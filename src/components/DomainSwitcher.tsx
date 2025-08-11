import React from 'react';
import { ToggleButton, ToggleButtonGroup } from '@mui/material';

interface DomainSwitcherProps {
  domain: 'retail' | 'insurance';
  onDomainChange: (domain: 'retail' | 'insurance') => void;
}

const DomainSwitcher: React.FC<DomainSwitcherProps> = ({ domain, onDomainChange }) => {
  return (
    <div>
      <div style={{
        fontWeight: 'bold',
        color: '#C6FF00',
        fontSize: 20,
        letterSpacing: 1,
        margin: '32px 0 24px 0',
        textAlign: 'center',
      }}>
        Domains
      </div>
      <ToggleButtonGroup
        value={domain}
        exclusive
        onChange={(_, value) => value && onDomainChange(value)}
        aria-label="Domain Switcher"
        sx={{ mb: 2 }}
      >
        <ToggleButton value="retail">Retail</ToggleButton>
        <ToggleButton value="insurance">Insurance</ToggleButton>
      </ToggleButtonGroup>
    </div>
  );
};

export default DomainSwitcher;
