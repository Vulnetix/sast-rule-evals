# vnx-llm-005 eval target
from langchain.tools import PythonREPLTool
from langchain.tools import BashProcess
from langchain_experimental.tools import PythonAstREPLTool
from langchain.chains import LLMMathChain
from langchain.agents import create_python_agent
from langchain.llms import OpenAI

# TRIGGERS: PythonREPLTool allows arbitrary Python execution
python_tool = PythonREPLTool()

# TRIGGERS: BashProcess allows arbitrary shell command execution
bash_tool = BashProcess()

# TRIGGERS: PythonAstREPLTool allows Python code execution
repl_tool = PythonAstREPLTool()

# TRIGGERS: LLMMathChain uses Python eval internally
llm = OpenAI(temperature=0)
math_chain = LLMMathChain(llm=llm)

# TRIGGERS: create_python_agent creates an agent with code execution capabilities
agent = create_python_agent(llm=OpenAI(), tool=PythonREPLTool(), verbose=True)

# Safe alternative: use purpose-built, sandboxed tools with strict input validation
# or run agent tools in an isolated container environment (Docker, gVisor)
