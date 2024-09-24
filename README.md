[![Multi-Modality](agorabanner.png)](https://discord.com/servers/agora-999382051935506503)

# Automated Prompt Engineering Hub

[![Join our Discord](https://img.shields.io/badge/Discord-Join%20our%20server-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/agora-999382051935506503) [![Subscribe on YouTube](https://img.shields.io/badge/YouTube-Subscribe-red?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@kyegomez3242) [![Connect on LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/kye-g-38759a207/) [![Follow on X.com](https://img.shields.io/badge/X.com-Follow-1DA1F2?style=for-the-badge&logo=x&logoColor=white)](https://x.com/kyegomezb)



# Install


```bash

$ pip install -U ape

```


## Usage

```python
from loguru import logger
from ape.auto_prompter import PromptBuilderAgent

# Example usage:
if __name__ == "__main__":
    # Configure loguru to output to a file as well as the console
    logger.add("agent_log.log", rotation="10 MB")
    
    
    # Initialize the prompt builder agent
    agent = PromptBuilderAgent()

    # Run the task multiple times (iterations parameter)
    task = "How can I establish a ROTH IRA to buy stocks and get a tax break? What are the criteria?"
    agent_name = "Financial-Analysis-Agent"

    # Example: Run the task 3 times and save the results to JSON
    prompts = agent.run_task(
        task=task, agent_name=agent_name, iterations=3
    )

    # Display the prompts in the log
    for prompt in prompts:
        logger.info(
            f"Prompt: {prompt.prompt}\nOutput: {prompt.output}\n"
        )


```