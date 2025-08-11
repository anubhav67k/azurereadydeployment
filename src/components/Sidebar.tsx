import React from 'react';
import './Sidebar.css';

interface SidebarProps {
  domain: 'retail' | 'insurance';
  onDomainChange: (domain: 'retail' | 'insurance') => void;
}

const Sidebar: React.FC<SidebarProps> = ({ domain, onDomainChange }) => {
  return (
    <div className="sidebar sidebar-hover-area">
      <div className="sidebar-label">Domains</div>
      <div className="sidebar-domain-switcher-vertical">
        <button
          className={`sidebar-domain-btn${domain === 'retail' ? ' selected' : ''}`}
          onClick={() => onDomainChange('retail')}
        >Retail</button>
        <button
          className={`sidebar-domain-btn${domain === 'insurance' ? ' selected' : ''}`}
          onClick={() => onDomainChange('insurance')}
        >Insurance</button>
      </div>
    </div>
  );
};

export default Sidebar;
