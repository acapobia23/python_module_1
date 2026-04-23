#!/usr/bin/env python3
"""
Test script to verify import structure and execution of all ft_*.py scripts
"""

import os
import sys
import subprocess
import re
import ast
from datetime import datetime
from pathlib import Path

# Add py06 to path to run the scripts
PY06_PATH = Path(__file__).parent / "py06"
sys.path.insert(0, str(PY06_PATH))

class ImportAnalyzer:
    """Analyzes import statements in Python files"""
    
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.tree = None
        self.imports = []
        self.parse()
    
    def parse(self):
        """Parse the Python file and extract import statements"""
        try:
            with open(self.filepath, 'r') as f:
                content = f.read()
            self.tree = ast.parse(content)
            self.extract_imports()
        except Exception as e:
            print(f"Error parsing {self.filepath}: {e}")
    
    def extract_imports(self):
        """Extract all import statements from AST"""
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    self.imports.append({
                        'type': 'import',
                        'module': alias.name,
                        'lineno': node.lineno
                    })
            elif isinstance(node, ast.ImportFrom):
                for alias in node.names:
                    self.imports.append({
                        'type': 'from...import',
                        'module': node.module,
                        'name': alias.name,
                        'lineno': node.lineno
                    })
    
    def get_import_structure(self) -> str:
        """Return the primary import structure used"""
        if not self.imports:
            return "No imports"
        
        types = [imp['type'] for imp in self.imports]
        if 'from...import' in types and 'import' not in types:
            return "from...import"
        elif 'import' in types and 'from...import' not in types:
            return "import"
        else:
            return "mixed"


class ScriptTestRunner:
    """Runs and validates test scripts"""
    
    # Expected behaviors
    EXPECTED_STRUCTURES = {
        'ft_alembic_0.py': ('import', 'elements'),
        'ft_alembic_1.py': ('from...import', 'elements'),
        'ft_alembic_2.py': ('import', 'alchemy.elements'),
        'ft_alembic_3.py': ('from...import', 'alchemy.elements'),
        'ft_alembic_4.py': ('import', 'alchemy'),
        'ft_alembic_5.py': ('from...import', 'alchemy'),
        'ft_distillation_0.py': ('from...import', 'alchemy.potions'),
        'ft_distillation_1.py': ('import', 'alchemy'),
        'ft_transmutation_0.py': ('import', 'alchemy.transmutation.recipes'),
        'ft_transmutation_1.py': ('import', 'alchemy.transmutation'),
        'ft_transmutation_2.py': ('import', 'alchemy'),
        'ft_kaboom_0.py': ('import', 'alchemy.grimoire'),
        'ft_kaboom_1.py': ('from...import', 'alchemy.grimoire.dark_spellbook'),
    }
    
    # Scripts that should fail
    SHOULD_FAIL = {'ft_alembic_4.py', 'ft_kaboom_1.py'}
    
    # Scripts that should succeed
    SHOULD_SUCCEED = set(EXPECTED_STRUCTURES.keys()) - SHOULD_FAIL
    
    def __init__(self, py06_path: Path):
        self.py06_path = py06_path
        self.results = []
    
    def check_import_structure(self, script_name: str) -> dict:
        """Check if import structure matches expectations"""
        script_path = self.py06_path / script_name
        result = {
            'script': script_name,
            'import_structure': 'N/A',
            'structure_expected': 'N/A',
            'structure_match': False,
            'error': None
        }
        
        try:
            analyzer = ImportAnalyzer(str(script_path))
            actual = analyzer.get_import_structure()
            expected_type, expected_module = self.EXPECTED_STRUCTURES[script_name]
            
            result['import_structure'] = actual
            result['structure_expected'] = expected_type
            result['structure_match'] = actual == expected_type
            
        except Exception as e:
            result['error'] = str(e)
        
        return result
    
    def run_script(self, script_name: str) -> dict:
        """Run a script and capture output/errors"""
        script_path = self.py06_path / script_name
        result = {
            'script': script_name,
            'execution': 'N/A',
            'output': '',
            'error': '',
            'returncode': None,
            'expected_fail': script_name in self.SHOULD_FAIL,
        }
        
        try:
            proc = subprocess.run(
                [sys.executable, str(script_path)],
                capture_output=True,
                text=True,
                timeout=10,
                cwd=str(self.py06_path)
            )
            
            result['output'] = proc.stdout
            result['error'] = proc.stderr
            result['returncode'] = proc.returncode
            
            # Determine if execution passed or failed as expected
            if script_name in self.SHOULD_FAIL:
                # These scripts SHOULD fail
                if proc.returncode != 0:
                    result['execution'] = 'PASS (failed as expected)'
                else:
                    result['execution'] = 'FAIL (should have failed)'
            else:
                # These scripts SHOULD succeed
                if proc.returncode == 0:
                    result['execution'] = 'PASS'
                else:
                    result['execution'] = 'FAIL'
        
        except subprocess.TimeoutExpired:
            result['error'] = 'Timeout'
            result['execution'] = 'FAIL'
        except Exception as e:
            result['error'] = str(e)
            result['execution'] = 'FAIL'
        
        return result
    
    def run_all_tests(self) -> list:
        """Run all tests and collect results"""
        results = []
        
        for script_name in sorted(self.EXPECTED_STRUCTURES.keys()):
            # Check structure
            struct_result = self.check_import_structure(script_name)
            
            # Run script
            exec_result = self.run_script(script_name)
            
            # Combine results
            combined = {**struct_result, **exec_result}
            results.append(combined)
        
        return results
    
    def generate_report(self, results: list) -> str:
        """Generate a formatted report"""
        report = []
        report.append("=" * 100)
        report.append(f"IMPORT SCRIPTS TEST REPORT - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("=" * 100)
        report.append("")
        
        # Summary
        structure_pass = sum(1 for r in results if r['structure_match'])
        structure_total = len(results)
        execution_pass = sum(1 for r in results if 'PASS' in r['execution'])
        execution_total = len(results)
        
        report.append("SUMMARY")
        report.append("-" * 100)
        report.append(f"Import Structure: {structure_pass}/{structure_total} PASSED")
        report.append(f"Script Execution: {execution_pass}/{execution_total} PASSED")
        report.append("")
        
        # Detailed results
        report.append("DETAILED RESULTS")
        report.append("-" * 100)
        
        for result in results:
            report.append(f"\n{result['script']}")
            report.append("~" * 80)
            
            # Import structure check
            struct_status = "✓ PASS" if result['structure_match'] else "✗ FAIL"
            report.append(f"  Import Structure: {struct_status}")
            report.append(f"    Expected: {result['structure_expected']}")
            report.append(f"    Actual:   {result['import_structure']}")
            
            # Execution check
            report.append(f"  Execution:       {result['execution']}")
            if result['expected_fail']:
                report.append(f"    (Expected to fail for pedagogical purposes)")
            
            # Output/Errors
            if result['output']:
                report.append(f"  Output:")
                for line in result['output'].split('\n')[:5]:  # First 5 lines
                    if line.strip():
                        report.append(f"    {line}")
                if len(result['output'].split('\n')) > 5:
                    report.append(f"    ...")
            
            if result['error']:
                report.append(f"  Error:")
                error_lines = result['error'].split('\n')
                for line in error_lines[:5]:  # First 5 lines
                    if line.strip():
                        report.append(f"    {line}")
                if len(error_lines) > 5:
                    report.append(f"    ...")
        
        report.append("")
        report.append("=" * 100)
        report.append(f"Test completed at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("=" * 100)
        
        return "\n".join(report)


def main():
    """Main test execution"""
    py06_path = Path(__file__).parent / "py06"
    
    if not py06_path.exists():
        print(f"Error: {py06_path} not found")
        sys.exit(1)
    
    print("Starting import scripts test...\n")
    
    runner = ScriptTestRunner(py06_path)
    results = runner.run_all_tests()
    report = runner.generate_report(results)
    
    # Print to console
    print(report)
    
    # Save to file with timestamp
    output_filename = f"output_test.txt"
    output_path = Path(__file__).parent / output_filename
    
    with open(output_path, 'w') as f:
        f.write(report)
    
    print(f"\n✓ Report saved to: {output_path}")


if __name__ == "__main__":
    main()
