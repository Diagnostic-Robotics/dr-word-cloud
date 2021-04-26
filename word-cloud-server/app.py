from flask import Flask

app = Flask(__name__)


@app.route('/')
def get_most_common_words():
	# Add your code here
	raise NotImplemented


if __name__ == '__main__':
	app.run()
