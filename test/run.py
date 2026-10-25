"""
🧭 Turn each JSON case into an independent unittest with clear
pass/fail reporting, level-order tree comparison, and a timeout guard.

Each case becomes a separate test method, allowing unittest to identify
the exact scenario that passed or failed in verbose mode.
"""

import sys
import json
import os
import time
import unittest
from collections import deque
from typing import Deque, Dict, List, Optional

from timeout_decorator import TimeoutError, timeout
from source.solution import Solution
from treenode import TreeNode


def _to_test_name(title: str) -> str:
    """🏷️ Convert a friendly test title into a valid unittest method name."""
    sanitized = ''.join(
        char.lower() if char.isalnum() else '_'
        for char in title
    )
    compact = '_'.join(
        part for part in sanitized.split('_') if part
    )
    return f'test_{compact}'


def _inplace_tree(root: Optional[TreeNode]) -> List[Optional[int]]:
    """🌳 Serialize a binary tree using level-order traversal.

    Missing children are represented by None. Trailing None values
    are removed to match LeetCode's standard tree representation.

    Args:
        root: Root node of the binary tree.

    Returns:
        Level-order list representing the tree structure.
    """
    if not root:
        return []

    result: List[Optional[int]] = []
    queue: Deque[Optional[TreeNode]] = deque([root])

    while queue:
        node = queue.popleft()

        if node is None:
            result.append(None)
            continue

        result.append(node.val)

        # Preserve the positions of missing children.
        queue.append(node.left)
        queue.append(node.right)

    # ✂️ Remove unnecessary None values at the end.
    while result and result[-1] is None:
        result.pop()

    return result


def _make_testcase(testcase):
    """🧱 Generate an independent unittest method from a JSON case."""

    def test_method(self):
        title: str = testcase['title']
        preorder: List[int] = testcase['input']['preorder']
        inorder: List[int] = testcase['input']['inorder']
        expected_output: List[Optional[int]] = testcase['output']
        description: str = testcase.get(
            'description',
            'No description provided.'
        )

        self._case_title = title
        self._case_description = description

        print('\n' + '=' * 60)
        print(f'🧪 Test Case : {title}')
        print(f'🤔 Scenario  : {description}')
        print(f'📝 Input     : preorder={preorder}, inorder={inorder}')
        print('⏳ Starting soon...')
        time.sleep(self.DISPLAY_DELAY_SECONDS)

        try:
            root: Optional[TreeNode] = self._run_case(
                preorder=preorder,
                inorder=inorder
            )
            actual_output: List[Optional[int]] = _inplace_tree(root)

        except TimeoutError:
            print(f'⏱️ Result    : Time Limit Exceeded in {title}')
            print('=' * 60)
            self.fail(f'⏱️ Time Limit Exceeded: {title}')

        if actual_output == expected_output:
            print(f'✅ Result    : Passed with answer {actual_output}')
        else:
            print(f'❌ Result    : Expected {expected_output}, got {actual_output}')

        print('=' * 60)
        time.sleep(self.DISPLAY_DELAY_SECONDS)

        self.assertEqual(
            actual_output,
            expected_output,
            f'❌ Value Mismatch in {title}\n'
            f'Expected = {expected_output}\n'
            f'Actual   = {actual_output}'
        )

    return test_method


class TestSolution(unittest.TestCase):
    """🧪 Test binary tree construction against JSON test cases."""

    # 🎛️ Adjust this delay for faster runs or more readable output.
    DISPLAY_DELAY_SECONDS = 2
    CASE_RESULTS: List[Dict[str, str]] = []

    def setUp(self):
        """🛠️ Create a fresh solution instance for every test."""
        self.__solution = Solution()
        return super().setUp()

    @timeout(1)
    def _run_case(
        self,
        preorder: List[int],
        inorder: List[int]
    ) -> Optional[TreeNode]:
        """⚡ Run one tree-construction case with a timeout guard."""
        return self.__solution.buildTree(
            preorder=preorder,
            inorder=inorder
        )


class ConstructBinaryTreeTestResult(unittest.TextTestResult):
    """🧾 Collect individual test outcomes for the final summary."""

    def addSuccess(self, test):
        super().addSuccess(test)
        TestSolution.CASE_RESULTS.append({
            'title': getattr(test, '_case_title', test._testMethodName),
            'status': '✅ Passed',
        })

    def addFailure(self, test, err):
        super().addFailure(test, err)
        TestSolution.CASE_RESULTS.append({
            'title': getattr(test, '_case_title', test._testMethodName),
            'status': '❌ Failed',
        })

    def addError(self, test, err):
        super().addError(test, err)
        TestSolution.CASE_RESULTS.append({
            'title': getattr(test, '_case_title', test._testMethodName),
            'status': '💥 Error',
        })

    def stopTestRun(self):
        super().stopTestRun()

        print('\n' + '🧾' + '=' * 58)
        print('🌳 Construct Binary Tree — Final Summary')

        if not TestSolution.CASE_RESULTS:
            print('No test cases were executed.')
            print('=' * 60)
            return

        results = TestSolution.CASE_RESULTS
        passed_count = sum(
            result['status'] == '✅ Passed' for result in results
        )
        failed_count = sum(
            result['status'] == '❌ Failed' for result in results
        )
        error_count = sum(
            result['status'] == '💥 Error' for result in results
        )
        success_rate = (passed_count / len(results)) * 100

        title_width = max(
            len('Test Case'),
            *(len(result['title']) for result in results)
        )
        status_width = max(
            len('Status'),
            *(len(result['status']) for result in results)
        )

        divider = f"+-{'-' * title_width}-+-{'-' * status_width}-+"
        header = (
            f"| {'Test Case'.ljust(title_width)} "
            f"| {'Status'.ljust(status_width)} |"
        )

        print(divider)
        print(header)
        print(divider)

        for result in results:
            print(
                f"| {result['title'].ljust(title_width)} "
                f"| {result['status'].ljust(status_width)} |"
            )

        print(divider)
        print(
            f'🏁 Total: {len(results)} | '
            f'✅ Passed: {passed_count} | '
            f'❌ Failed: {failed_count} | '
            f'💥 Errors: {error_count}'
        )
        print(f'📈 Success Rate: {success_rate:.2f}%')
        print('=' * 60)


# 🚦 Select the appropriate test suite.
is_pr_run = '--pr' in sys.argv

if is_pr_run:
    sys.argv.remove('--pr')

_CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
_FILE_NAME = 'cases_pr.json' if is_pr_run else 'cases.json'
_FILE_PATH = os.path.join(_CURRENT_DIRECTORY, _FILE_NAME)

with open(_FILE_PATH, mode='r', encoding='utf-8') as read_file:
    all_testcases = json.load(read_file)

    # 🧪 Register every JSON case as an independent unittest.
    for testcase in all_testcases:
        test_name = _to_test_name(testcase['title'])

        if hasattr(TestSolution, test_name):
            raise ValueError(f'Duplicate test title: {testcase["title"]}')

        setattr(
            TestSolution,
            test_name,
            _make_testcase(testcase)
        )


if __name__ == '__main__':
    unittest.main(
        verbosity=2,
        testRunner=unittest.TextTestRunner(
            resultclass=ConstructBinaryTreeTestResult
        )
    )
