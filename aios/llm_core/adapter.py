
from aios.llm_core.cores.base import BaseLLM
from aios.llm_core.registry import MODEL_REGISTRY


class LLMAdapter:
    """Parameters for LLMs

    Args:
        llm_name (str): Name of the LLMs
        max_gpu_memory (dict, optional): Maximum GPU resources that can be allocated to the LLM. Defaults to None.
        eval_device (str, optional): Evaluation device of binding LLM to designated devices for inference. Defaults to None.
        max_new_tokens (int, optional): Maximum token length generated by the LLM. Defaults to 256.
        log_mode (str, optional): Mode of logging the LLM processing status. Defaults to "console".
        use_backend (str, optional): Backend to use for speeding up open-source LLMs. Defaults to None. Choices are ["vllm", "ollama"]
    """

    def __init__(self,
                 llm_name: str,
                 max_gpu_memory: dict = None,
                 eval_device: str = None,
                 max_new_tokens: int = 256,
                 log_mode: str = "console",
                 use_backend: str = None,
                 use_context_manager: bool = False
        ):

        self.model: BaseLLM = None

        # For API-based LLM
        if llm_name in MODEL_REGISTRY.keys():
            self.model = MODEL_REGISTRY[llm_name](
                llm_name = llm_name,
                log_mode = log_mode,
                use_context_manager = use_context_manager
            )
        # For locally-deployed LLM
        else:
            if use_backend == "ollama" or llm_name.startswith("ollama"):
                pass
                #ollama here
            elif use_backend == "vllm":
                # VLLM here
                pass
            else: # use huggingface LLM without backend
                pass
                

    def address_syscall(self,
                        llm_syscall,
                        temperature=0.0) -> None:
        """Address request sent from the agent

        Args:
            agent_request: AgentProcess object that contains request sent from the agent
            temperature (float, optional): Parameter to control the randomness of LLM output. Defaults to 0.0.
        """
        return self.model.address_syscall(llm_syscall, temperature)


    