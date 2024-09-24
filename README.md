# Automated Prompt Engineering Hub

[![Join our Discord](https://img.shields.io/badge/Discord-Join%20our%20server-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/agora-999382051935506503) [![Subscribe on YouTube](https://img.shields.io/badge/YouTube-Subscribe-red?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@kyegomez3242) [![Connect on LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/kye-g-38759a207/) [![Follow on X.com](https://img.shields.io/badge/X.com-Follow-1DA1F2?style=for-the-badge&logo=x&logoColor=white)](https://x.com/kyegomezb)


**PromptBuilderAgent** is an enterprise-focused, robust Python library designed for large-scale, multi-agent orchestration with LLMs (Large Language Models). It enables organizations to efficiently generate dynamic, task-specific prompts for LLM agents, with built-in features for validation, logging, and performance monitoring.


## Key Features

- **Multiple Prompt Generation**: Create and execute prompts for multiple agents in parallel or sequential iterations.
- **Enterprise-Grade Reliability**: Integrated logging with Loguru for detailed tracking, performance monitoring, and error management.
- **Pydantic-Based Validation**: Ensure data integrity and type safety with powerful Pydantic validation.
- **Scalable Execution**: Run tasks across multiple iterations, capturing outputs, errors, and metadata for each run.
- **JSON Prompt Storage**: Save each task's prompt and output to structured JSON files for auditability and reproducibility.
- **UUID and Timestamp Tracking**: Every prompt is uniquely identified with a UUID and timestamp, providing full traceability for enterprise environments.
- **Flexible Integration with LLM Agents**: Seamlessly integrates with popular LLM models like GPT-4 for task execution, making it easy to deploy within any LLM-based architecture.



<!-- 
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






 -->

## Installation

To get started, you can install the **PromptBuilderAgent** library via pip:

```bash
pip install prompt-builder-agent
```

You'll also need to set up the following environment variables:

1. **OpenAI API Key**: Set your OpenAI API key as an environment variable to allow the agent to communicate with GPT models.

```bash
export OPENAI_API_KEY="your-openai-api-key"
```

Alternatively, you can create a `.env` file and add the following:

```
OPENAI_API_KEY=your-openai-api-key
```

## Quick Start

Here’s a quick example to help you get started with **PromptBuilderAgent**:

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
```

## Use Cases

**PromptBuilderAgent** is designed for enterprises and developers building multi-agent systems powered by LLMs. Key use cases include:

- **Automated Prompt Generation**: Streamline LLM-driven workflows by dynamically generating prompts based on tasks.
- **Task-Specific Agents**: Create agents tailored to specific business functions such as finance, marketing, and customer support.
- **Auditability and Compliance**: All prompts and outputs are saved to JSON with UUIDs and timestamps, providing a transparent audit trail.
- **Scalability in AI Operations**: Ideal for companies managing multiple agents or AI-driven processes that require repetitive tasks or workflows.

## Advanced Features

### Multiple Agent Support

**PromptBuilderAgent** allows you to generate prompts for multiple agents with ease. Each agent can have its own tasks, and you can run them concurrently or sequentially with iterations.

```python
prompts = agent.run_task(task="Analyze stock performance", agent_name="Stock-Analysis-Agent", iterations=5)
```

### Iterations for Task Execution

You can specify how many times a task should be executed, enabling A/B testing, prompt refinement, or batch task processing.

```python
prompts = agent.run_task(task="Generate a financial report", agent_name="Finance-Agent", iterations=10)
```

### JSON Storage

Each prompt and its corresponding output is saved as a JSON file with detailed metadata such as a UUID, timestamp, agent name, and more. This ensures full auditability of your LLM-driven operations.

```bash
{
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "timestamp": "2024-09-24T12:34:56Z",
    "agent_name": "Finance-Agent",
    "task": "Generate a financial report",
    "prompt": "The user wants to generate a financial report...",
    "output": "Here is your financial report..."
}
```

## Logging and Error Handling

**PromptBuilderAgent** leverages `loguru` for advanced logging and error management. All key operations, including prompt generation, agent execution, and errors, are logged for transparency and debugging.

Example log output:

```bash
2024-09-24 14:35:12 | INFO | Initialized PromptBuilderAgent successfully.
2024-09-24 14:35:13 | INFO | Running task 'Generate a financial report' for agent 'Finance-Agent'...
2024-09-24 14:35:15 | SUCCESS | Task executed successfully for iteration 1.
```

You can configure the logging to suit your enterprise needs by specifying different log levels, rotation policies, and formats.

## Contributing

We welcome contributions from the open-source community and enterprise partners. If you're interested in improving this project or adding features, feel free to submit a pull request or raise an issue.

To get started:

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact Us

For enterprise inquiries, custom integration support, or licensing, please contact:

**Email**: enterprise@promptbuilder.com  
**Website**: [promptbuilder.com](https://promptbuilder.com)

---

With **PromptBuilderAgent**, enterprises can unlock the full potential of LLM agents by automating prompt generation and scaling AI-driven workflows efficiently. Start using the tool today to supercharge your multi-agent system operations.

---