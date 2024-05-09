
import numpy as np
import matplotlib.pyplot as plt

class Agent:
    def __init__(self, position, destination):
        self.position = np.array(position, dtype=float)
        self.destination = np.array(destination, dtype=float)
        self.velocity = np.array([0.0, 0.0], dtype=float)

    def update(self, dt):
        # Calculate direction to destination
        direction = self.destination - self.position
        distance = np.linalg.norm(direction)

        # Calculate speed based on distance to destination
        if distance > 0.1:
            self.velocity = 2.0 * direction / distance
        else:
            self.velocity = np.array([0.0, 0.0])

        # Update position based on speed and time
        self.position += self.velocity * dt

def simulate_crowd(num_agents, num_steps):
    agents = [Agent(np.random.rand(2) * 10, np.random.rand(2) * 10) for _ in range(num_agents)]

    for _ in range(num_steps):
        plt.clf()
        plt.xlim(0, 10)
        plt.ylim(0, 10)

        for agent in agents:
            agent.update(0.1)
            plt.plot(agent.position[0], agent.position[1], 'bo')

        plt.pause(0.01)


simulate_crowd(num_agents=1000, num_steps=1200)
plt.show()
