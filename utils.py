"""
Utility classes for code comparison and analysis.

This module provides tools for analyzing and comparing code structures,
functionality, and quality.
"""

import re
from typing import Dict, List, Set, Tuple, Any
from collections import defaultdict


class CodeComparator:
    """
    A utility class for comparing code snippets and identifying differences.
    
    Provides methods to compare code structure, functionality, and find
    similarities and differences between code blocks.
    """
    
    def __init__(self):
        """Initialize the CodeComparator."""
        pass
    
    def compare_code(self, code1: str, code2: str) -> Dict[str, Any]:
        """
        Compare two code snippets and return a detailed comparison report.
        
        Args:
            code1 (str): First code snippet to compare
            code2 (str): Second code snippet to compare
            
        Returns:
            Dict[str, Any]: Comparison report with metrics and differences
        """
        return {
            "identical": code1 == code2,
            "similarity_score": self._calculate_similarity(code1, code2),
            "structural_diff": self._compare_structure(code1, code2),
            "line_diff": self._compare_lines(code1, code2)
        }
    
    def _calculate_similarity(self, code1: str, code2: str) -> float:
        """
        Calculate similarity score between two code snippets.
        
        Args:
            code1 (str): First code snippet
            code2 (str): Second code snippet
            
        Returns:
            float: Similarity score between 0.0 and 1.0
        """
        lines1 = set(code1.strip().split('\n'))
        lines2 = set(code2.strip().split('\n'))
        
        if not lines1 and not lines2:
            return 1.0
        
        intersection = len(lines1 & lines2)
        union = len(lines1 | lines2)
        
        return intersection / union if union > 0 else 0.0
    
    def _compare_structure(self, code1: str, code2: str) -> Dict[str, Any]:
        """
        Compare structural elements of two code snippets.
        
        Args:
            code1 (str): First code snippet
            code2 (str): Second code snippet
            
        Returns:
            Dict[str, Any]: Structural comparison details
        """
        return {
            "functions_in_code1": self._extract_functions(code1),
            "functions_in_code2": self._extract_functions(code2),
            "classes_in_code1": self._extract_classes(code1),
            "classes_in_code2": self._extract_classes(code2),
            "imports_in_code1": self._extract_imports(code1),
            "imports_in_code2": self._extract_imports(code2)
        }
    
    def _compare_lines(self, code1: str, code2: str) -> Dict[str, List[str]]:
        """
        Compare code on a line-by-line basis.
        
        Args:
            code1 (str): First code snippet
            code2 (str): Second code snippet
            
        Returns:
            Dict[str, List[str]]: Lines unique to each code snippet
        """
        lines1 = code1.strip().split('\n')
        lines2 = code2.strip().split('\n')
        
        set1 = set(lines1)
        set2 = set(lines2)
        
        return {
            "only_in_code1": list(set1 - set2),
            "only_in_code2": list(set2 - set1),
            "common_lines": list(set1 & set2)
        }
    
    def _extract_functions(self, code: str) -> List[str]:
        """
        Extract function names from code.
        
        Args:
            code (str): Code snippet
            
        Returns:
            List[str]: List of function names
        """
        pattern = r'def\s+(\w+)\s*\('
        return re.findall(pattern, code)
    
    def _extract_classes(self, code: str) -> List[str]:
        """
        Extract class names from code.
        
        Args:
            code (str): Code snippet
            
        Returns:
            List[str]: List of class names
        """
        pattern = r'class\s+(\w+)\s*[\(:]'
        return re.findall(pattern, code)
    
    def _extract_imports(self, code: str) -> List[str]:
        """
        Extract import statements from code.
        
        Args:
            code (str): Code snippet
            
        Returns:
            List[str]: List of import statements
        """
        pattern = r'(?:from|import)\s+[\w.]+'
        return re.findall(pattern, code)


class CodeAnalyzer:
    """
    A utility class for analyzing code quality, complexity, and patterns.
    
    Provides methods to assess code structure, identify potential issues,
    and gather metrics about code quality.
    """
    
    def __init__(self):
        """Initialize the CodeAnalyzer."""
        self.complexity_threshold = 10
    
    def analyze_code(self, code: str) -> Dict[str, Any]:
        """
        Perform comprehensive analysis of code.
        
        Args:
            code (str): Code snippet to analyze
            
        Returns:
            Dict[str, Any]: Comprehensive analysis report
        """
        return {
            "lines_of_code": self._count_lines(code),
            "complexity": self._calculate_complexity(code),
            "functions": self._analyze_functions(code),
            "classes": self._analyze_classes(code),
            "documentation_coverage": self._calculate_doc_coverage(code),
            "code_quality_issues": self._identify_quality_issues(code)
        }
    
    def _count_lines(self, code: str) -> Dict[str, int]:
        """
        Count different types of lines in code.
        
        Args:
            code (str): Code snippet
            
        Returns:
            Dict[str, int]: Line counts
        """
        lines = code.split('\n')
        code_lines = 0
        comment_lines = 0
        blank_lines = 0
        
        for line in lines:
            stripped = line.strip()
            if not stripped:
                blank_lines += 1
            elif stripped.startswith('#'):
                comment_lines += 1
            else:
                code_lines += 1
        
        return {
            "total": len(lines),
            "code": code_lines,
            "comments": comment_lines,
            "blank": blank_lines
        }
    
    def _calculate_complexity(self, code: str) -> Dict[str, Any]:
        """
        Calculate code complexity metrics.
        
        Args:
            code (str): Code snippet
            
        Returns:
            Dict[str, Any]: Complexity metrics
        """
        conditionals = len(re.findall(r'\b(if|elif|else|for|while|try|except)\b', code))
        nested_depth = self._calculate_nesting_depth(code)
        
        complexity_score = conditionals + (nested_depth * 2)
        
        return {
            "conditional_count": conditionals,
            "nesting_depth": nested_depth,
            "complexity_score": complexity_score,
            "is_complex": complexity_score > self.complexity_threshold
        }
    
    def _calculate_nesting_depth(self, code: str) -> int:
        """
        Calculate maximum nesting depth in code.
        
        Args:
            code (str): Code snippet
            
        Returns:
            int: Maximum nesting depth
        """
        max_depth = 0
        current_depth = 0
        
        for char in code:
            if char in '({[':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char in ')}]':
                current_depth -= 1
        
        return max_depth
    
    def _analyze_functions(self, code: str) -> List[Dict[str, Any]]:
        """
        Analyze individual functions in code.
        
        Args:
            code (str): Code snippet
            
        Returns:
            List[Dict[str, Any]]: Function analysis details
        """
        pattern = r'def\s+(\w+)\s*\((.*?)\):'
        matches = re.finditer(pattern, code)
        
        functions = []
        for match in matches:
            func_name = match.group(1)
            params = [p.strip() for p in match.group(2).split(',') if p.strip()]
            
            functions.append({
                "name": func_name,
                "parameters": params,
                "parameter_count": len(params)
            })
        
        return functions
    
    def _analyze_classes(self, code: str) -> List[Dict[str, Any]]:
        """
        Analyze classes in code.
        
        Args:
            code (str): Code snippet
            
        Returns:
            List[Dict[str, Any]]: Class analysis details
        """
        pattern = r'class\s+(\w+)(?:\((.*?)\))?:'
        matches = re.finditer(pattern, code)
        
        classes = []
        for match in matches:
            class_name = match.group(1)
            base_classes = [b.strip() for b in match.group(2).split(',') if match.group(2) and b.strip()]
            
            classes.append({
                "name": class_name,
                "base_classes": base_classes,
                "base_class_count": len(base_classes)
            })
        
        return classes
    
    def _calculate_doc_coverage(self, code: str) -> Dict[str, Any]:
        """
        Calculate documentation coverage in code.
        
        Args:
            code (str): Code snippet
            
        Returns:
            Dict[str, Any]: Documentation coverage metrics
        """
        docstring_count = len(re.findall(r'""".*?"""', code, re.DOTALL))
        function_count = len(re.findall(r'\bdef\s+\w+', code))
        class_count = len(re.findall(r'\bclass\s+\w+', code))
        
        total_items = function_count + class_count
        documented_items = docstring_count
        
        coverage_percentage = (documented_items / total_items * 100) if total_items > 0 else 0
        
        return {
            "documented_items": documented_items,
            "total_items": total_items,
            "coverage_percentage": round(coverage_percentage, 2)
        }
    
    def _identify_quality_issues(self, code: str) -> List[str]:
        """
        Identify potential code quality issues.
        
        Args:
            code (str): Code snippet
            
        Returns:
            List[str]: List of identified issues
        """
        issues = []
        
        # Check for very long lines
        lines = code.split('\n')
        for i, line in enumerate(lines, 1):
            if len(line) > 120:
                issues.append(f"Line {i}: Very long line ({len(line)} characters)")
        
        # Check for missing docstrings
        functions = re.finditer(r'def\s+(\w+)\s*\(.*?\):', code)
        for match in functions:
            func_start = match.end()
            # Simple check: look for docstring right after function definition
            next_lines = code[func_start:func_start+200]
            if not re.match(r'\s*"""', next_lines) and not re.match(r"\s*'''", next_lines):
                issues.append(f"Function '{match.group(1)}': Missing docstring")
        
        # Check for bare except clauses
        if re.search(r'\bexcept\s*:', code):
            issues.append("Found bare 'except:' clause - should specify exception type")
        
        return issues
