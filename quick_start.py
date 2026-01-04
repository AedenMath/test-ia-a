"""
Quick Start Guide for AutoModifyingAI

This module demonstrates basic usage of the AutoModifyingAI class.
"""

from auto_modifying_ai import AutoModifyingAI


def main():
    """
    Example 1: Basic initialization and simple task
    """
    print("=" * 60)
    print("Example 1: Basic Initialization")
    print("=" * 60)
    
    # Initialize AutoModifyingAI
    ai = AutoModifyingAI(
        model="gpt-4",
        temperature=0.7,
        max_iterations=5
    )
    
    # Execute a simple task
    response = ai.execute_task("Write a simple hello world function in Python")
    print(f"Response:\n{response}\n")
    
    
    def example_2():
        """
        Example 2: Advanced usage with custom parameters
        """
        print("=" * 60)
        print("Example 2: Advanced Configuration")
        print("=" * 60)
        
        ai = AutoModifyingAI(
            model="gpt-4",
            temperature=0.5,
            max_iterations=10,
            timeout=30
        )
        
        # Execute a more complex task
        task = "Create a Python class for managing a to-do list with add, remove, and list methods"
        response = ai.execute_task(task)
        print(f"Response:\n{response}\n")
    
    
    def example_3():
        """
        Example 3: Iterative improvement
        """
        print("=" * 60)
        print("Example 3: Iterative Improvement")
        print("=" * 60)
        
        ai = AutoModifyingAI(
            model="gpt-4",
            temperature=0.3,
            max_iterations=15
        )
        
        # Start with initial code
        initial_prompt = "Write a function that calculates fibonacci numbers"
        
        # Execute and get improved versions
        result = ai.execute_task(initial_prompt)
        print(f"Improved Result:\n{result}\n")
    
    
    def example_4():
        """
        Example 4: Working with file paths
        """
        print("=" * 60)
        print("Example 4: File-Based Tasks")
        print("=" * 60)
        
        ai = AutoModifyingAI(
            model="gpt-4",
            temperature=0.6,
            max_iterations=8
        )
        
        # Task that involves file manipulation
        task = "Create a Python script that reads a CSV file and outputs a summary"
        response = ai.execute_task(task)
        print(f"Response:\n{response}\n")
    
    
    def example_5():
        """
        Example 5: Error handling and validation
        """
        print("=" * 60)
        print("Example 5: Error Handling")
        print("=" * 60)
        
        try:
            ai = AutoModifyingAI(
                model="gpt-4",
                temperature=0.7,
                max_iterations=5
            )
            
            # Execute task with error handling
            response = ai.execute_task("Write unit tests for a calculator class")
            print(f"Response:\n{response}\n")
            
        except Exception as e:
            print(f"Error occurred: {type(e).__name__}: {e}\n")
    
    
    # Run all examples
    example_2()
    example_3()
    example_4()
    example_5()


if __name__ == "__main__":
    main()
