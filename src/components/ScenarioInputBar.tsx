import React from 'react';
import { Box, TextField, Button, MenuItem, Select, InputLabel, FormControl } from '@mui/material';

interface ScenarioInputBarProps {
  scenario: string;
  setScenario: (s: string) => void;
  demoQuestions: string[];
  onSubmit: () => void;
  selectedDemo: string;
  setSelectedDemo: (s: string) => void;
}

const ScenarioInputBar: React.FC<ScenarioInputBarProps> = ({ scenario, setScenario, demoQuestions, onSubmit, selectedDemo, setSelectedDemo }) => {
  const handleDemoChange = (event: any) => {
    setSelectedDemo(event.target.value);
    setScenario(event.target.value);
  };

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setScenario(e.target.value);
    if (selectedDemo) setSelectedDemo('');
  };

  return (
    <Box sx={{ display: 'flex', alignItems: 'center', mb: 2, gap: 2, background: '#23272F', borderRadius: 2, p: 2 }}>
      <FormControl sx={{ minWidth: 300, background: '#292d36', borderRadius: 1 }} size="small">
        <InputLabel sx={{ color: '#fff' }}>Select a demo question</InputLabel>
        <Select
          value={selectedDemo}
          label="Select a demo question"
          onChange={handleDemoChange}
          sx={{ color: '#fff', '.MuiOutlinedInput-notchedOutline': { borderColor: '#444' }, '.MuiSvgIcon-root': { color: '#fff' } }}
          MenuProps={{
            PaperProps: {
              style: {
                backgroundColor: '#23272F',
                color: '#fff',
                maxHeight: 150, // About 3 items tall
                overflowY: 'auto',
              },
            },
          }}
        >
          {demoQuestions.map((q, idx) => (
            <MenuItem value={q} key={idx} sx={{ color: '#fff', background: '#23272F', '&.Mui-selected': { background: '#333' } }}>{q}</MenuItem>
          ))}
        </Select>
      </FormControl>
      <TextField
        size="small"
        sx={{ flex: 1, background: '#292d36', borderRadius: 1, input: { color: '#fff' } }}
        placeholder="Or type your own scenario.."
        value={scenario}
        onChange={handleInputChange}
        InputProps={{ style: { color: '#fff' } }}
      />
      <Button variant="contained" color="primary" sx={{ height: 40, px: 4, fontWeight: 'bold' }} onClick={() => {
        onSubmit();
        setScenario('');
        setSelectedDemo('');
      }}>
        Send
      </Button>
    </Box>
  );
};

export default ScenarioInputBar;
