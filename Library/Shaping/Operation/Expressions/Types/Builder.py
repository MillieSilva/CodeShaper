## System Imports
from typing import TYPE_CHECKING


## Application Imports
if TYPE_CHECKING:
	from Library.Shaping.Operation.Actions.Types import BuilderAction

from Library.Shaping.Operation.Expressions.base import BaseExpression
from Library.Shaping.Operation.Actions.interfaces import ActionInterface


## Library Imports
import regex


class BuilderExpression(BaseExpression):
	
	def __init__(self, action: 'BuilderAction', parent: ActionInterface):
		super().__init__(action, parent)
		
		self.action = action
		
	def process_expression(self):
		if self.groups:
			return
		
		self.groups = []
		self.names = []
		
		for match in regex.finditer(self.action.builder.match, self.parent.content):
			self.groups.append(match.groups())
			self.names.append(match.re.groupindex)
	
	def resolve_expression(self, content: str) -> str:
		result = self.action.Expression
		
		for expression in self.Frames:
			result = expression.resolve_expression(content)
		
		return result
	
