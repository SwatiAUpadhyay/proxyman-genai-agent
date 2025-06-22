from agent.agent_runner import run_agent
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    print("\n🔧 Proxyman Log Agent Ready!")
    user_input = input("\nAsk for logs (e.g., 'Get logs for Amazon app on Android emulator'): ")
    result = run_agent(user_input)
    print("\n📦 Result:\n")
    print(result)
