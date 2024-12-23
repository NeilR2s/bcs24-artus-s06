import time

class QueueApp:
    def __init__(self):
        self.task_queue = []

    def add_task(self, task, priority=0):
        self.task_queue.append((task, priority))
        print(f"Task added: {task} (Priority: {priority})")
        time.sleep(1)
        self.task_queue.sort(key=lambda x: x[1]) 
        return self.task_queue

    def process_task(self):
        if not self.task_queue:
            print("No tasks to process.")
            return

        current_task = self.task_queue.pop(0)
        print(f"Processing task: {current_task[0]} (Priority: {current_task[1]})")
        time.sleep(1)

    def dequeue(self):
        if not self.task_queue:
            print("No tasks to remove.")
            return None

        dequeued_task = self.task_queue.pop(0)
        print(f"Task Completed: {dequeued_task[0]} (Priority: {dequeued_task[1]})")
        time.sleep(1)
        return dequeued_task
    
    def remaining_task(self):
        print("Tasks Remaining:", len(self.task_queue))
        return len(self.task_queue)
    
scheduler = QueueApp()

scheduler.add_task("Jakul", priority=2)
scheduler.add_task("Salsalani", priority=3)
scheduler.add_task("Abdul", priority=1)

scheduler.remaining_task()

scheduler.dequeue()
scheduler.remaining_task()

scheduler.dequeue()
scheduler.remaining_task()

scheduler.dequeue()
scheduler.remaining_task()

scheduler.process_task()
