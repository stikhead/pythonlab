def task_scheduler():
    """
    Interactive Command-Line Task Scheduler demonstrating lazy evaluation,
    Boolean logic, and nested conditional statements.
    """
    queue = []
    
    print("=== Interactive Task Scheduler ===")
    
    while True:
        print("\nOptions: [1] Add Task  [2] Evaluate Next Task  [3] View Queue  [4] Exit")
        choice = input("Enter choice (1-4): ").strip()
    
        if choice == '4':
            print("Exiting scheduler. Goodbye!")
            break
            
        elif choice == '1':
            task_name = input("Enter task name: ").strip()
            is_urgent = input("Is the task urgent? (y/n): ").strip().lower() == 'y'
            is_important = input("Is the task important? (y/n): ").strip().lower() == 'y'
            has_resources = input("Do we have resources for it right now? (y/n): ").strip().lower() == 'y'
            
            queue.append({
                'name': task_name,
                'urgent': is_urgent,
                'important': is_important,
                'resources': has_resources
            })
            print(f"Task '{task_name}' added to the queue.")
            
        elif choice == '2':
            if not queue:
                print("The task queue is currently empty.")
            else:
                current_task = queue.pop(0)
                name = current_task['name']
                urgent = current_task['urgent']
                important = current_task['important']
                resources = current_task['resources']
                
                print(f"\nEvaluating Task: '{name}'")
                if urgent and important:
                    if resources:
                        print(f"[ACTION] Executing '{name}' immediately! (Critical priority)")
                    else:
                        print(f"[ACTION] '{name}' is critical, but we lack resources. Escalating!")
                        
                elif urgent or important:
                    print(f"[ACTION] Scheduling '{name}' for later today. (Normal priority)")
                    
                elif not urgent and not important:
                    print(f"[ACTION] Dropping '{name}'. (Low priority, NOT urgent and NOT important)")
                    
                else:
                    print(f"[ACTION] Pushing '{name}' to the backlog.")
                    
        elif choice == '3':
            if not queue:
                print("Queue is empty.")
            else:
                print("\nCurrent Queue:")
                for i, task in enumerate(queue):
                    print(f"  {i+1}. {task['name']} (Urgent: {task['urgent']}, Important: {task['important']})")
                    
        else:
            print("Invalid input. Please select a valid option from 1 to 4.")

if __name__ == "__main__":
    task_scheduler()