import requests

API_URL = "https://jsonplaceholder.typicode.com/todos"


def get_recent_todos(limit=200) -> list[dict]:
    """Get the 200 most recent TODOs"""
    response = requests.get(API_URL)
    response.raise_for_status()
    todos = response.json()
    return todos[:limit]


def create_todo(title:str, completed=False, user_id=1) -> dict:
    """Create a new TODO"""
    payload = {
        'userId': user_id,
        'title': title,
        'completed': completed
    }
    response = requests.post(API_URL, json=payload)
    response.raise_for_status()
    return response.json()


def delete_todo(todo_id:int) -> bool:
    """Delete a TODO by ID"""
    response = requests.delete(f"{API_URL}/{todo_id}")
    response.raise_for_status()
    return response.status_code == 200



if __name__ == "__main__":
    print("=== API Interaction Demo ===\n")
    
    # 1. Get 200 most recent TODOs
    print("1. Fetching 200 most recent TODOs...")
    todos = get_recent_todos(200)
    print(f"   Retrieved {len(todos)} TODOs")
    print(f"   First TODO: {todos[0]}")
    print(f"   Last TODO: {todos[-1]}\n")
    
    # 2. Create a TODO
    print("2. Creating a new TODO...")
    new_todo = create_todo("Complete interview exercise", completed=True)
    print(f"   Created TODO: {new_todo}\n")
    
    # 3. Delete a TODO
    print("3. Deleting TODO with ID 1...")
    deleted = delete_todo(1)
    print(f"   Deleted: {deleted}\n")


