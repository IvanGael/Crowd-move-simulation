import numpy as np
import matplotlib.pyplot as plt

class Agent:
    def __init__(self, position, destination, obstacles, other_agents):
        self.position = np.array(position, dtype=float)
        self.destination = np.array(destination, dtype=float)
        self.velocity = np.array([0.0, 0.0], dtype=float)
        self.obstacles = obstacles
        self.other_agents = other_agents

    def update(self, dt):
        # Calculate direction towards destination
        direction = self.destination - self.position
        distance = np.linalg.norm(direction)

        # Obstacle avoidance
        avoidance = np.zeros_like(direction)
        for obstacle in self.obstacles:
            vec_to_obstacle = obstacle - self.position
            distance_to_obstacle = np.linalg.norm(vec_to_obstacle)
            if distance_to_obstacle < 1.0:  # Arbitrary threshold
                avoidance -= 10.0 * vec_to_obstacle / distance_to_obstacle**2

        # Collision avoidance with other agents
        collision_avoidance = np.zeros_like(direction)
        for other_agent in self.other_agents:
            if other_agent != self:
                vec_to_other = other_agent.position - self.position
                distance_to_other = np.linalg.norm(vec_to_other)
                if distance_to_other < 1.0:  # Arbitrary threshold
                    collision_avoidance -= 10.0 * vec_to_other / distance_to_other**2

        # Goal seeking behavior
        goal_direction = self.destination - self.position
        goal_direction /= np.linalg.norm(goal_direction)
        self.velocity = goal_direction + avoidance + collision_avoidance

        # Update position based on velocity and time
        self.position += self.velocity * dt

def simulate_crowd(num_agents, num_steps):
    obstacles = [np.array([5.0, 5.0])]  # Adding obstacle
    agents = [Agent(np.random.rand(2) * 10, np.random.rand(2) * 10, obstacles, []) for _ in range(num_agents)]

    for step in range(num_steps):
        plt.clf()
        plt.xlim(0, 10)
        plt.ylim(0, 10)

        # Update agents' destinations dynamically
        if step % 100 == 0:  # Change destination every 100 steps
            new_destinations = [np.random.rand(2) * 10 for _ in range(num_agents)]
            for agent, new_destination in zip(agents, new_destinations):
                agent.destination = new_destination

        # Update list of other agents for each agent
        for agent in agents:
            agent.other_agents = [other_agent for other_agent in agents if other_agent != agent]

        for agent in agents:
            agent.update(0.1)
            plt.plot(agent.position[0], agent.position[1], 'bo')

        plt.plot(obstacles[0][0], obstacles[0][1], 'ro')  # Plot obstacles
        plt.pause(0.01)

simulate_crowd(num_agents=100, num_steps=500)
plt.show()
