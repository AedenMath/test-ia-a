"""
Quick Start Test Suite for AutoModifyingAI

This module provides simple tests to verify the AutoModifyingAI system works correctly.
Run this file to test all core functionality.
"""

import sys
from auto_modifying_ai import AutoModifyingAI


def test_basic_initialization():
    """Test 1: Basic initialization of AutoModifyingAI"""
    print("\n" + "="*70)
    print("TEST 1: Basic Initialization")
    print("="*70)
    
    ai = AutoModifyingAI(name="TestAI")
    
    assert ai.name == "TestAI", "Name should be 'TestAI'"
    assert ai.version == "1.0.0", "Version should be '1.0.0'"
    assert ai.modifications_count == 0, "Initial modifications should be 0"
    
    print(f"✅ AI Instance Created: {ai}")
    print(f"   Name: {ai.name}")
    print(f"   Version: {ai.version}")
    print(f"   Modifications: {ai.modifications_count}")
    
    return ai


def test_add_method(ai):
    """Test 2: Adding a new method dynamically"""
    print("\n" + "="*70)
    print("TEST 2: Adding Dynamic Method")
    print("="*70)
    
    # Define a new method as a string
    new_method_code = """
def greet(self, name):
    return f"Hello, {name}! I am {self.name}"
"""
    
    print("Adding method: greet(name)")
    success = ai.add_method("greet", new_method_code)
    
    assert success, "Method should be added successfully"
    assert hasattr(ai, "greet"), "AI should have greet method"
    
    # Test the new method
    result = ai.greet("Developer")
    print(f"✅ Method added successfully!")
    print(f"   Result: {result}")
    
    assert result == "Hello, Developer! I am TestAI", "Greet method should work correctly"


def test_code_execution(ai):
    """Test 3: Execute arbitrary code"""
    print("\n" + "="*70)
    print("TEST 3: Code Execution")
    print("="*70)
    
    code = """
x = 10
y = 20
result = x + y
"""
    
    print("Executing code: x=10, y=20, result=x+y")
    ai.execute_code(code)
    
    print("✅ Code executed successfully!")


def test_learning_from_feedback(ai):
    """Test 4: Learning from feedback"""
    print("\n" + "="*70)
    print("TEST 4: Learning from Feedback")
    print("="*70)
    
    ai.learn_from_feedback("First execution completed successfully", True)
    ai.learn_from_feedback("Second execution had issues", False)
    ai.learn_from_feedback("Third execution improved", True)
    
    print("✅ Feedback recorded:")
    for i, history in enumerate(ai.learning_history, 1):
        print(f"   {i}. {history['feedback']} - Success: {history['success']}")


def test_performance_summary(ai):
    """Test 5: Get performance summary"""
    print("\n" + "="*70)
    print("TEST 5: Performance Summary")
    print("="*70)
    
    summary = ai.get_performance_summary()
    
    print("✅ Performance Summary:")
    print(f"   Name: {summary['name']}")
    print(f"   Version: {summary['version']}")
    print(f"   Modifications: {summary['modifications']}")
    print(f"   Learning Events: {summary['learning_events']}")
    print(f"   Success Rate: {summary['success_rate']:.1%}")


def test_modify_method(ai):
    """Test 6: Modify existing method"""
    print("\n" + "="*70)
    print("TEST 6: Modifying Existing Method")
    print("="*70)
    
    # Modify the greet method
    modified_code = """
def greet(self, name):
    return f"Greetings, {name}! I am {self.name} v{self.version} 🤖"
"""
    
    print("Modifying greet method...")
    success = ai.modify_method("greet", modified_code)
    
    assert success, "Method should be modified successfully"
    
    result = ai.greet("User")
    print(f"✅ Method modified successfully!")
    print(f"   New Result: {result}")


def run_all_tests():
    """Run all tests in sequence"""
    print("\n")
    print("╔" + "="*68 + "╗")
    print("║" + " "*15 + "🚀 AutoModifyingAI Test Suite 🚀" + " "*20 + "║")
    print("╚" + "="*68 + "╝")
    
    try:
        # Run all tests
        ai = test_basic_initialization()
        test_add_method(ai)
        test_code_execution(ai)
        test_learning_from_feedback(ai)
        test_performance_summary(ai)
        test_modify_method(ai)
        
        # Final summary
        print("\n" + "="*70)
        print("✅ ALL TESTS PASSED!")
        print("="*70)
        print("\n📊 Final AI State:")
        print(f"   {ai}")
        print(f"   Total Modifications: {ai.modifications_count}")
        print(f"   Total Learning Events: {len(ai.learning_history)}")
        
        return True
        
    except AssertionError as e:
        print(f"\n❌ TEST FAILED: {e}")
        return False
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
