# import kivy

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (NumericProperty, ReferenceListProperty, ObjectProperty)
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint, random
# from kivy.uix.label import Label
# kivy.require('2.1.0') # replace with your current kivy version !

class PongPaddle(Widget):
    score = NumericProperty(0)

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * vx, vy)
            vel = bounced * 1.1
            ball.velocity = vel.x, vel.y + offset

class PongBall(Widget):
    # velocity of the ball on x and y axis
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    # referencelist property so we can use ball.velocity as
    # a shorthand, just like e.g. w.pos for w.x and w.y
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    # ``move`` function will move the ball one step. This
    #  will be called in equal intervals to animate the ball
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

class Window(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)

    def serve_ball(self, vel=(4,randint(-2,2))):
        self.ball.center = self.center
        # self.ball.velocity = Vector(4, 0).rotate(randint(0, 360))
        self.ball.velocity = vel

    def update(self, dt):
        # call e.g. ball.move
        self.ball.move()
        """
        # Code that ball bounces at walls if no users would exist 
        # bounce off top and bottom
        if (self.ball.y < 0) or (self.ball.top > self.height):
            self.ball.velocity_y *= -1
        # bounce off left and right
        if (self.ball.x < 0) or (self.ball.right > self.width):
            self.ball.velocity_x *= -1
        """
        # bounce off paddles
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)

        # bounce off top and bottom
        if (self.ball.y < 0) or (self.ball.top > self.height):
            self.ball.velocity_y *= -1

        # went off to a side to score point?
        if self.ball.x < self.x:
            self.player2.score += 1
            self.serve_ball(vel=(4, 1))
        if self.ball.right > self.width:
            self.player1.score += 1
            self.serve_ball(vel=(-4, -1))


    def on_touch_move(self, touch):
        if touch.x < self.width / 3:
            self.player1.center_y = touch.y
        if touch.x > self.width - self.width / 3:
            self.player2.center_y = touch.y


class MyWindowApp(App):

    def build(self):
        # Creating a reference to the main widget is obligatory
        # Just using Window() instead is not creating action
        window_ref = Window()
        Clock.schedule_interval(window_ref.update, 1.0/60.0)
        window_ref.serve_ball((4,randint(-2,2)))
        return window_ref
        # return Label(text='Hello world')

if __name__ == '__main__':
    MyWindowApp().run()