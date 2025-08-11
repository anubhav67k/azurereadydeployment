import React from 'react';
import { Paper, Typography } from '@mui/material';

interface AgentLogProps {
  logs: string[];
}

const AgentLog: React.FC<AgentLogProps> = ({ logs }) => (
  <Paper sx={{ p: 2 }}>
    <Typography variant="h6">Agent Logs</Typography>
    <ul>
      {logs.map((log, i) => <li key={i}>{log}</li>)}
    </ul>
  </Paper>
);

export default AgentLog;
