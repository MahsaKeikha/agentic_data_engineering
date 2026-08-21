from typing import Any
from .base import BaseAgent
from ..skills import review_contract, analyze_lineage, evaluate_quality, review_transformations, assess_reliability
from ..tools import contract_record, lineage_graph, quality_report, transformation_plan, reliability_plan
class ContractAgent(BaseAgent):
 name="data_contract";responsibility="Validate schema, ownership and SLA contract.";required_skills=("review_contract",);allowed_tools=("contract_record",)
 def run(self,s:Any):
  a=review_contract(contract_record(s.case));s.analyses[self.name]=a;s.unresolved_questions.extend(a["questions"]);s.record(self.name,"reviewed data contract",a)
class LineageAgent(BaseAgent):
 name="lineage";responsibility="Analyze sources, transformations and downstream consumers.";required_skills=("analyze_lineage",);allowed_tools=("lineage_graph",)
 def run(self,s:Any):
  a=analyze_lineage(lineage_graph(s.case));s.analyses[self.name]=a;s.unresolved_questions.extend(a["questions"]);s.record(self.name,"analyzed lineage",a)
class QualityAgent(BaseAgent):
 name="quality";responsibility="Evaluate quality rules and observed failures.";required_skills=("evaluate_quality",);allowed_tools=("quality_report",)
 def run(self,s:Any):
  a=evaluate_quality(quality_report(s.case));s.analyses[self.name]=a;s.unresolved_questions.extend(a["questions"]);s.risks.extend(a["risks"]);s.record(self.name,"evaluated data quality",a)
class TransformationAgent(BaseAgent):
 name="transformation";responsibility="Review transformation intent and test coverage.";required_skills=("review_transformations",);allowed_tools=("transformation_plan",)
 def run(self,s:Any):
  a=review_transformations(transformation_plan(s.case));s.analyses[self.name]=a;s.risks.extend(a["risks"]);s.record(self.name,"reviewed transformations",a)
class ReliabilityAgent(BaseAgent):
 name="reliability";responsibility="Assess scheduling, retry and recovery controls.";required_skills=("assess_reliability",);allowed_tools=("reliability_plan",)
 def run(self,s:Any):
  a=assess_reliability(reliability_plan(s.case));s.analyses[self.name]=a;s.risks.extend(a["risks"]);s.record(self.name,"assessed reliability",a)
CLASSES=[ContractAgent,LineageAgent,QualityAgent,TransformationAgent,ReliabilityAgent]
def build_agents():return [c() for c in CLASSES]
AGENT_MANIFEST=[{"name":c.name,"responsibility":c.responsibility,"skills":list(c.required_skills),"tools":list(c.allowed_tools)} for c in CLASSES]
