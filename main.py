from flask import Flask, request

fuck = Flask(__name__)

@fuck.route('/welcome', methods=['GET'])
def welcome():
    name = request.args.get('name')
    return f'{name} Welcome!'

if __name__ == '__main__':
   fuck.run(debug=True)
