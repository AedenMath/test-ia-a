"""
Advanced Usage Examples for AutoModifyingAI System

This module demonstrates advanced patterns and techniques for working with
the AutoModifyingAI system, including self-modification, learning, and
adaptive behavior patterns.
"""

from typing import Any, Callable, Dict, List, Optional
import json
from datetime import datetime


class AutoModifyingAI:
    """
    Advanced example of an AI system capable of self-modification and learning.
    """
    
    def __init__(self, name: str, version: str = "1.0.0"):
        self.name = name
        self.version = version
        self.knowledge_base: Dict[str, Any] = {}
        self.behavior_rules: List[Dict[str, Any]] = []
        self.performance_metrics: Dict[str, float] = {}
        self.modification_history: List[Dict[str, Any]] = []
        
    def learn_from_interaction(self, user_input: str, feedback: str) -> None:
        """
        Learn from user interactions and feedback to improve responses.
        
        Args:
            user_input: The input from the user
            feedback: Feedback on the quality of the response
        """
        learning_record = {
            "timestamp": datetime.utcnow().isoformat(),
            "input": user_input,
            "feedback": feedback,
            "processed": True
        }
        
        key = f"interaction_{len(self.knowledge_base)}"
        self.knowledge_base[key] = learning_record
        
        self._update_behavior_rules(feedback)
    
    def _update_behavior_rules(self, feedback: str) -> None:
        """
        Update internal behavior rules based on feedback.
        
        Args:
            feedback: User feedback for behavior adjustment
        """
        rule = {
            "type": "adaptive_rule",
            "feedback_source": feedback,
            "created_at": datetime.utcnow().isoformat(),
            "active": True
        }
        self.behavior_rules.append(rule)
        
        self._record_modification("behavior_update", rule)
    
    def _record_modification(self, modification_type: str, modification_data: Dict[str, Any]) -> None:
        """
        Record all modifications for traceability and debugging.
        
        Args:
            modification_type: Type of modification made
            modification_data: Details of the modification
        """
        modification_record = {
            "type": modification_type,
            "timestamp": datetime.utcnow().isoformat(),
            "data": modification_data,
            "version": self.version
        }
        self.modification_history.append(modification_record)
    
    def self_optimize(self) -> None:
        """
        Perform self-optimization based on collected metrics and rules.
        This is an advanced feature that allows the system to improve itself.
        """
        if not self.performance_metrics:
            return
        
        avg_performance = sum(self.performance_metrics.values()) / len(self.performance_metrics)
        
        optimization = {
            "type": "self_optimization",
            "avg_performance": avg_performance,
            "rules_count": len(self.behavior_rules),
            "timestamp": datetime.utcnow().isoformat()
        }
        
        self._record_modification("optimization_cycle", optimization)
    
    def add_custom_behavior(self, behavior_name: str, behavior_func: Callable) -> None:
        """
        Dynamically add custom behaviors to the system.
        
        Args:
            behavior_name: Name identifier for the behavior
            behavior_func: Callable that implements the behavior
        """
        behavior = {
            "name": behavior_name,
            "type": "custom_behavior",
            "callable": behavior_func.__name__,
            "added_at": datetime.utcnow().isoformat()
        }
        self.behavior_rules.append(behavior)
        self._record_modification("behavior_addition", behavior)
    
    def get_modification_report(self) -> Dict[str, Any]:
        """
        Generate a comprehensive report of all modifications.
        
        Returns:
            Dictionary containing modification statistics and history
        """
        return {
            "system_name": self.name,
            "version": self.version,
            "total_modifications": len(self.modification_history),
            "behavior_rules_count": len(self.behavior_rules),
            "knowledge_items": len(self.knowledge_base),
            "modification_types": list(set(
                mod["type"] for mod in self.modification_history
            )),
            "recent_modifications": self.modification_history[-5:] if self.modification_history else []
        }


# Example 1: Basic Initialization and Learning
def example_basic_learning():
    """Example: Creating an AI system and teaching it from interactions."""
    print("=" * 60)
    print("Example 1: Basic Learning Loop")
    print("=" * 60)
    
    ai = AutoModifyingAI("LearnBot", version="1.0.0")
    
    # Simulate learning from interactions
    interactions = [
        ("What is machine learning?", "Good explanation, clear and concise"),
        ("How does neural networks work?", "Excellent technical depth"),
        ("Explain quantum computing", "Could be more beginner-friendly")
    ]
    
    for user_input, feedback in interactions:
        ai.learn_from_interaction(user_input, feedback)
    
    print(f"System learned from {len(ai.knowledge_base)} interactions")
    print(f"Generated {len(ai.behavior_rules)} behavior rules\n")


# Example 2: Advanced Self-Modification
def example_self_modification():
    """Example: Demonstrating self-modification capabilities."""
    print("=" * 60)
    print("Example 2: Self-Modification Cycle")
    print("=" * 60)
    
    ai = AutoModifyingAI("AdaptiveBot", version="2.0.0")
    
    # Add performance metrics
    ai.performance_metrics = {
        "response_quality": 0.87,
        "user_satisfaction": 0.92,
        "accuracy": 0.89,
        "response_time": 0.95
    }
    
    # Run optimization
    ai.self_optimize()
    
    # Add custom behaviors
    def safety_check():
        return True
    
    def content_filter():
        return True
    
    ai.add_custom_behavior("safety_check", safety_check)
    ai.add_custom_behavior("content_filter", content_filter)
    
    # Generate report
    report = ai.get_modification_report()
    print(json.dumps(report, indent=2))
    print()


# Example 3: Complex Behavior Integration
def example_complex_behaviors():
    """Example: Integrating complex adaptive behaviors."""
    print("=" * 60)
    print("Example 3: Complex Behavior Integration")
    print("=" * 60)
    
    ai = AutoModifyingAI("ComplexBot", version="3.0.0")
    
    # Define complex behavior functions
    def context_aware_learning():
        return {"context_level": "advanced", "adaptation": True}
    
    def multi_modal_processing():
        return {"modes": ["text", "image", "audio"], "enabled": True}
    
    def predictive_optimization():
        return {"prediction_confidence": 0.94, "next_actions": []}
    
    # Add behaviors
    behaviors = [
        ("context_aware_learning", context_aware_learning),
        ("multi_modal_processing", multi_modal_processing),
        ("predictive_optimization", predictive_optimization)
    ]
    
    for name, func in behaviors:
        ai.add_custom_behavior(name, func)
    
    # Simulate learning cycles
    for i in range(3):
        ai.learn_from_interaction(
            f"Complex query {i+1}",
            "Positive feedback with high confidence"
        )
        ai.self_optimize()
    
    print(f"Integrated {len(ai.behavior_rules)} complex behaviors")
    print(f"Completed {len([m for m in ai.modification_history if m['type'] == 'optimization_cycle'])} optimization cycles")
    print()


# Example 4: Modification History and Traceability
def example_modification_tracking():
    """Example: Tracking and analyzing modification history."""
    print("=" * 60)
    print("Example 4: Modification History Tracking")
    print("=" * 60)
    
    ai = AutoModifyingAI("TrackedBot", version="1.5.0")
    
    # Create various modifications
    ai.learn_from_interaction("User input 1", "Great response")
    ai.add_custom_behavior("test_behavior", lambda: True)
    ai.learn_from_interaction("User input 2", "Excellent")
    ai.self_optimize()
    ai.learn_from_interaction("User input 3", "Perfect")
    
    # Analyze modification history
    print(f"Total modifications: {len(ai.modification_history)}")
    print("\nModification Timeline:")
    
    for i, mod in enumerate(ai.modification_history, 1):
        print(f"  {i}. [{mod['type']}] at {mod['timestamp']}")
    
    print()


# Example 5: Performance Monitoring and Reporting
def example_performance_monitoring():
    """Example: Monitoring system performance and generating reports."""
    print("=" * 60)
    print("Example 5: Performance Monitoring")
    print("=" * 60)
    
    ai = AutoModifyingAI("PerformanceBot", version="2.1.0")
    
    # Simulate performance metrics collection
    metrics_history = [
        {"response_quality": 0.80, "efficiency": 0.75},
        {"response_quality": 0.85, "efficiency": 0.80},
        {"response_quality": 0.90, "efficiency": 0.88}
    ]
    
    for metrics in metrics_history:
        ai.performance_metrics.update(metrics)
        ai.self_optimize()
    
    # Generate comprehensive report
    report = ai.get_modification_report()
    
    print("Performance Report:")
    print(json.dumps(report, indent=2))
    print()


def main():
    """Run all advanced examples."""
    print("\n")
    print("*" * 60)
    print("AutoModifyingAI System - Advanced Usage Examples")
    print("*" * 60)
    print("\n")
    
    example_basic_learning()
    example_self_modification()
    example_complex_behaviors()
    example_modification_tracking()
    example_performance_monitoring()
    
    print("*" * 60)
    print("All examples completed successfully!")
    print("*" * 60)
    print("\n")


if __name__ == "__main__":
    main()
