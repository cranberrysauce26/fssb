import bdb

class Tracer(bdb.Bdb):
    def user_return(self, frame, return_value):
        print("RETURNING", return_value)
    def user_line(self, frame):
        print("IN USER LINE")


if __name__ == '__main__':
    t = Tracer()
    code = open("test2.py").read()
    t.run(code)

# import subprocess
# subprocess.run(['touch', '/home/steven/projects/fssb/HEY.txt'])
# import os

# print(os.getcwd())
# os.chdir('/home/steven/Desktop/testdir')
# os.rename('testdir','awesome_dir')
# os.remove('a.cpp')
# print(os.listdir())
# os.makedirs("/home/steven/projects/fssb/BAD")

# from flask import Flask, request, render_template

# app = Flask(__name__)

# app.debug = True

# @app.route('/')
# def index():
# 	return 'INDEX'

# # https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html
# app.run()