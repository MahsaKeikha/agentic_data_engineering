class PipelineMemory:
 def __init__(self):self.snapshots=[]
 def add(self,snapshot):self.snapshots.append(snapshot)
 def snapshot(self):return list(self.snapshots)
