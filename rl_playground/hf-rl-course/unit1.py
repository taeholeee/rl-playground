import gym
from huggingface_sb3 import package_to_hub
from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.vec_env import DummyVecEnv

# Create the environment
env = make_vec_env("LunarLander-v2", n_envs=16)
model = PPO(
    policy="MlpPolicy",
    env=env,
    verbose=1,
)
# Train it for 1,000,000 timesteps
model.learn(total_timesteps=1000000)
# Save the model
model_name = "ppo-LunarLander-v2"
model.save(model_name)

# Create a new environment for evaluation
eval_env = gym.make("LunarLander-v2")
# Evaluate the model with 10 evaluation episodes and deterministic=True
mean_reward, std_reward = evaluate_policy(
    model, eval_env, n_eval_episodes=10, deterministic=True
)
print(f"mean_reward={mean_reward:.2f} +/- {std_reward}")

# PLACE the variables you've just defined two cells above
# Define the name of the environment
env_id = "LunarLander-v2"

# TODO: Define the model architecture we used
model_architecture = "PPO"

## Define a repo_id
## repo_id is the id of the model repository from the Hugging Face Hub (repo_id = {organization}/{repo_name} for instance ThomasSimonini/ppo-LunarLander-v2
## CHANGE WITH YOUR REPO ID
repo_id = (
    "theolee/ppo-LunarLander-v2"  # Change with your repo id, you can't push with mine 😄
)

## Define the commit message
commit_message = "Upload PPO LunarLander-v2 trained agent"

# Create the evaluation env
eval_env = DummyVecEnv([lambda: gym.make(env_id)])

# PLACE the package_to_hub function you've just filled here
package_to_hub(
    model=model,  # Our trained model
    model_name=model_name,  # The name of our trained model
    model_architecture=model_architecture,  # The model architecture we used: in our case PPO
    env_id=env_id,  # Name of the environment
    eval_env=eval_env,  # Evaluation Environment
    repo_id=repo_id,  # id of the model repository from the Hugging Face Hub (repo_id = {organization}/{repo_name} for instance ThomasSimonini/ppo-LunarLander-v2
    commit_message=commit_message,
)
