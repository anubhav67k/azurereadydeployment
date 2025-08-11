import React from 'react';
import ReactFlow, { Background, Controls } from 'reactflow';
import type { Node, Edge } from 'reactflow';
import 'reactflow/dist/style.css';

interface AgentNetworkProps {
  nodes: Node[];
  edges: Edge[];
}

const AgentNetwork: React.FC<AgentNetworkProps> = ({ nodes, edges }) => {
  return (
    <div style={{ width: '100%', height: 400, position: 'relative' }}>
      <style>{`.react-flow__attribution { display: none !important; }`}</style>
      <ReactFlow nodes={nodes} edges={edges} fitView>
        <Controls />
        <Background />
      </ReactFlow>
    </div>
  );
};

export default AgentNetwork;
