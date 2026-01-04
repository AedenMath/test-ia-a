"""
AutoModifyingAI class implementation.

This module provides an intelligent AI system capable of self-modification
and autonomous learning through code generation and execution.
"""

import ast
import inspect
import os
from typing import Any, Callable, Dict, List, Optional


class AutoModifyingAI:
    """
    An AI system that can autonomously modify its own code and functionality.
    
    This class implements a self-improving AI that can:
    - Generate and execute code dynamically
    - Modify its own methods and attributes
    - Learn from execution results
    - Improve performance over time
    """
    
    def __init__(self, name: str = "AutoModifyingAI"):
        """
        Initialize the AutoModifyingAI instance.
        
        Args:
            name: Name identifier for this AI instance
        """
        self.name = name
        self.version = "1.0.0"
        self.learning_history: List[Dict[str, Any]] = []
        self.modifications_count = 0
        self.performance_metrics = {}
    
    def add_method(self, method_name: str, method_code: str) -> bool:
        """
        Dynamically add a new method to the AI instance.
        
        Args:
            method_name: Name of the method to add
            method_code: Python code string defining the method
            
        Returns:
            bool: True if method was added successfully, False otherwise
        """
        try:
            # Create a namespace for execution
            namespace = {'self': self}
            
            # Execute the method code
            exec(method_code, namespace)
            
            # Get the method from the namespace
            method = namespace.get(method_name)
            
            if callable(method):
                setattr(self, method_name, method.__get__(self, type(self)))
                self.modifications_count += 1
                return True
            return False
        except Exception as e:
            print(f"Error adding method {method_name}: {e}")
            return False
    
    def modify_method(self, method_name: str, new_code: str) -> bool:
        """
        Modify an existing method in the AI instance.
        
        Args:
            method_name: Name of the method to modify
            new_code: New Python code string for the method
            
        Returns:
            bool: True if method was modified successfully, False otherwise
        """
        if not hasattr(self, method_name):
            print(f"Method {method_name} does not exist")
            return False
        
        try:
            # Store the old method for rollback if needed
            old_method = getattr(self, method_name)
            
            # Add the modified method
            if self.add_method(method_name, new_code):
                self.learning_history.append({
                    'action': 'modify',
                    'method': method_name,
                    'timestamp': self._get_timestamp()
                })
                return True
            else:
                return False
        except Exception as e:
            print(f"Error modifying method {method_name}: {e}")
            return False
    
    def execute_code(self, code: str, context: Optional[Dict[str, Any]] = None) -> Any:
        """
        Execute arbitrary Python code in a controlled environment.
        
        Args:
            code: Python code string to execute
            context: Optional dictionary of variables available to the code
            
        Returns:
            The result of the code execution
        """
        try:
            namespace = {'self': self}
            if context:
                namespace.update(context)
            
            exec(code, namespace)
            return namespace.get('result', None)
        except Exception as e:
            print(f"Error executing code: {e}")
            return None
    
    def learn_from_feedback(self, feedback: str, success: bool) -> None:
        """
        Learn from execution feedback to improve future performance.
        
        Args:
            feedback: Feedback string describing the execution result
            success: Boolean indicating if the execution was successful
        """
        self.learning_history.append({
            'feedback': feedback,
            'success': success,
            'timestamp': self._get_timestamp()
        })
    
    def get_performance_summary(self) -> Dict[str, Any]:
        """
        Get a summary of the AI's performance metrics.
        
        Returns:
            Dictionary containing performance statistics
        """
        successful_feedback = sum(
            1 for item in self.learning_history 
            if item.get('success', False)
        )
        total_feedback = len(self.learning_history)
        
        return {
            'name': self.name,
            'version': self.version,
            'modifications': self.modifications_count,
            'learning_events': total_feedback,
            'success_rate': successful_feedback / total_feedback if total_feedback > 0 else 0,
            'performance_metrics': self.performance_metrics
        }
    
    def _get_timestamp(self) -> str:
        """
        Get the current timestamp.
        
        Returns:
            str: Current timestamp as ISO format string
        """
        from datetime import datetime
        return datetime.utcnow().isoformat()
    
    def __repr__(self) -> str:
        """Return string representation of the AI instance."""
        return f"AutoModifyingAI(name='{self.name}', version='{self.version}', modifications={self.modifications_count})"
    
    def __str__(self) -> str:
        """Return human-readable string representation of the AI instance."""
        return f"{self.name} v{self.version} - Modifications: {self.modifications_count}"
