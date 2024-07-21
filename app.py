from flask import Flask, render_template, request, jsonify
import simpy
import random

app = Flask(__name__)

class Household:
    def __init__(self, env):
        self.env = env
        self.money = 1000

    def earn_wages(self, amount):
        self.money += amount
        yield self.env.timeout(1)

class Producer:
    def __init__(self, env):
        self.env = env
        self.profit = 0

    def produce_goods(self):
        self.profit += random.randint(50, 150)
        yield self.env.timeout(1)

def run_simulation(env):
    household = Household(env)
    producer = Producer(env)
    while True:
        env.process(household.earn_wages(100))
        env.process(producer.produce_goods())
        yield env.timeout(1)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_simulation', methods=['POST'])
def run_sim():
    simulation_time = int(request.form.get('time', 100))
    env = simpy.Environment()
    env.process(run_simulation(env))
    env.run(until=simulation_time)
    return jsonify({"status": "Simulation completed"})

if __name__ == '__main__':
    app.run(debug=True)
