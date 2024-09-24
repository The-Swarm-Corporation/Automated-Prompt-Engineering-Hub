import os
import json
import uuid
from pydantic import BaseModel, Field
from typing import List, Optional
from loguru import logger
from datetime import datetime
from ape.prompt_generator_agent import prompt_generator_agent
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


# Define schema for agent prompt using Pydantic
class AgentPrompt(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: str = Field(
        default_factory=lambda: datetime.utcnow().isoformat()
    )
    agent_name: str
    task: str
    prompt: str
    output: Optional[str] = None

    class Config:
        """Config to handle non-JSON serializable objects."""

        json_encoders = {
            datetime: lambda v: v.isoformat(),
        }


class PromptBuilderAgent:
    def __init__(
        self,
    ):
        logger.info("Initializing the PromptBuilderAgent...")

        # Initialize the master agent
        self.master_agent = prompt_generator_agent

        logger.success("Agent initialized successfully")

    def run_task(
        self, task: str, agent_name: str, iterations: int = 1
    ) -> List[AgentPrompt]:
        """
        Runs a task multiple times (based on iterations) and generates prompts for each iteration.
        Saves the prompts and outputs to a JSON file.
        """
        logger.info(
            f"Running task '{task}' for agent '{agent_name}' with {iterations} iterations."
        )
        prompts = []

        for i in range(iterations):
            logger.info(f"Iteration {i+1} for task: {task}")
            # Generate the prompt
            prompt_template = self._generate_prompt_template(
                task, agent_name
            )

            try:
                # Execute the task using the master agent
                output = self.master_agent.run(task)
                prompt_template.output = output
                logger.success(
                    f"Task executed successfully for iteration {i+1}"
                )
            except Exception as e:
                logger.error(
                    f"Error executing task for iteration {i+1}: {e}"
                )
                prompt_template.output = None

            # Append the generated prompt and result
            prompts.append(prompt_template)

        # Save prompts to JSON
        self._save_prompts_to_json(prompts, agent_name)

        return prompts

    def _generate_prompt_template(
        self, task: str, agent_name: str
    ) -> AgentPrompt:
        """
        Generates a prompt with a unique ID, timestamp, and the task description.
        The master agent will handle the primary task, output format, constraints, and exception handling.
        """
        logger.info("Generating prompt template...")

        # Let the master agent handle the full prompt generation
        context = f"The user wants to accomplish the following task: {task}."

        # Return a Pydantic AgentPrompt object with context
        return AgentPrompt(
            agent_name=agent_name, task=task, prompt=context
        )

    def _save_prompts_to_json(
        self, prompts: List[AgentPrompt], agent_name: str
    ) -> None:
        """
        Saves the generated prompts and outputs to a JSON file.
        """
        logger.info(f"Saving {len(prompts)} prompts to JSON file...")
        # Convert Pydantic models to dictionaries
        prompts_dict = [prompt.dict() for prompt in prompts]

        # Save to a file (filename includes the agent name and timestamp)
        filename = f"{agent_name}_prompts_{datetime.utcnow().isoformat()}.json"
        with open(filename, "w") as f:
            json.dump(prompts_dict, f, indent=4)

        logger.success(f"Prompts saved to {filename}.")


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
