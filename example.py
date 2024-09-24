from loguru import logger
from ape.auto_prompter import PromptBuilderAgent

# Example usage:
if __name__ == "__main__":
    # Configure loguru to output to a file as well as the console
    logger.add("agent_log.log", rotation="10 MB")

    # Get the OpenAI API key from the environment variable
    api_key = os.getenv("OPENAI_API_KEY")

    if api_key is None:
        logger.error(
            "OPENAI_API_KEY is not set in environment variables."
        )
        exit(1)

    # Initialize the prompt builder agent
    agent = PromptBuilderAgent(api_key=api_key)

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
