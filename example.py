from loguru import logger
from ape.auto_prompter import PromptBuilderAgent

# Example usage:
if __name__ == "__main__":
    # Configure loguru to output to a file as well as the console
    logger.add("agent_log.log", rotation="10 MB")
    
    
    # Initialize the prompt builder agent
    agent = PromptBuilderAgent()

    # Run the task multiple times (iterations parameter)
    task = "Generate an system prompt for an agent analyzes balance sheets"
    agent_name = "Balance-Sheet-Agent-1"

    # Example: Run the task 3 times and save the results to JSON
    prompts = agent.run_task(
        task=task, agent_name=agent_name, iterations=3
    )

    # Display the prompts in the log
    for prompt in prompts:
        logger.info(
            f"Prompt: {prompt.prompt}\nOutput: {prompt.output}\n"
        )
