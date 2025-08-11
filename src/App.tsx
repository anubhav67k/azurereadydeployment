import React, { useState, useEffect } from 'react';
import Sidebar from './components/Sidebar';
import ScenarioInputBar from './components/ScenarioInputBar';
import AgentNetwork from './components/AgentNetwork';
import AgentLog from './components/AgentLog';
import './App.css';
import type { Node, Edge } from 'reactflow';

// Demo questions
import retailDemoQuestionsJson from './retail_demo_questions.json';
import insuranceDemoQuestionsJson from './insurance_demo_questions.json';

const retailDemoQuestions: string[] = retailDemoQuestionsJson;
const insuranceDemoQuestions: string[] = insuranceDemoQuestionsJson;

// Retail network
const retailNodes: Node[] = [
  { id: 'returns_manager', position: { x: 400, y: 60 }, data: { label: 'returns_manager' }, style: { background: '#90caf9', color: '#23272F' } },
  { id: 'ecommerce_manager', position: { x: 120, y: 200 }, data: { label: 'ecommerce_manager' }, style: { background: '#90caf9', color: '#23272F' } },
  { id: 'marketing_manager', position: { x: 180, y: 350 }, data: { label: 'marketing_manager' }, style: { background: '#90caf9', color: '#23272F' } },
  { id: 'customer_service_rep', position: { x: 350, y: 200 }, data: { label: 'customer_service_rep' }, style: { background: '#90caf9', color: '#23272F' } },
  { id: 'product_specialist', position: { x: 520, y: 150 }, data: { label: 'product_specialist' }, style: { background: '#ef5350', color: '#fff' } },
  { id: 'order_fulfillment_coordinator', position: { x: 400, y: 350 }, data: { label: 'order_fulfillment_coordinator' }, style: { background: '#90caf9', color: '#23272F' } },
  { id: 'merchandising_manager', position: { x: 600, y: 300 }, data: { label: 'merchandising_manager' }, style: { background: '#90caf9', color: '#23272F' } },
  { id: 'logistics_coordinator', position: { x: 400, y: 480 }, data: { label: 'logistics_coordinator' }, style: { background: '#90caf9', color: '#23272F' } },
  { id: 'warehouse_manager', position: { x: 700, y: 170 }, data: { label: 'warehouse_manager' }, style: { background: '#90caf9', color: '#23272F' } },
  { id: 'inventory_manager', position: { x: 870, y: 230 }, data: { label: 'inventory_manager' }, style: { background: '#90caf9', color: '#23272F' } },
];
const retailEdges: Edge[] = [
  { id: 'e_csr_returns', source: 'customer_service_rep', target: 'returns_manager', animated: false },
  { id: 'e_csr_ecom', source: 'customer_service_rep', target: 'ecommerce_manager', animated: false },
  { id: 'e_csr_marketing', source: 'customer_service_rep', target: 'marketing_manager', animated: false },
  { id: 'e_csr_ofc', source: 'customer_service_rep', target: 'order_fulfillment_coordinator', animated: false },
  { id: 'e_csr_product', source: 'customer_service_rep', target: 'product_specialist', animated: false },
  { id: 'e_product_warehouse', source: 'product_specialist', target: 'warehouse_manager', animated: false },
  { id: 'e_product_merch', source: 'product_specialist', target: 'merchandising_manager', animated: false },
  { id: 'e_product_inventory', source: 'product_specialist', target: 'inventory_manager', animated: false },
  { id: 'e_ofc_logistics', source: 'order_fulfillment_coordinator', target: 'logistics_coordinator', animated: false },
  { id: 'e_warehouse_inventory', source: 'warehouse_manager', target: 'inventory_manager', animated: false },
  { id: 'e_merch_inventory', source: 'merchandising_manager', target: 'inventory_manager', animated: false },
];

// Insurance network
const insuranceNodes: Node[] = [
  { id: 'legal_counsel', position: { x: 400, y: 60 }, data: { label: 'legal_counsel' }, style: { background: '#90caf9', color: '#23272F' } },
  { id: 'claims_adjuster', position: { x: 400, y: 180 }, data: { label: 'claims_adjuster' }, style: { background: '#90caf9', color: '#23272F' } },
  { id: 'claims_supervisor', position: { x: 260, y: 260 }, data: { label: 'claims_supervisor' }, style: { background: '#90caf9', color: '#23272F' } },
  { id: 'senior_claims_manager', position: { x: 260, y: 400 }, data: { label: 'senior_claims_manager' }, style: { background: '#ef5350', color: '#fff' } },
  { id: 'risk_manager', position: { x: 400, y: 480 }, data: { label: 'risk_manager' }, style: { background: '#90caf9', color: '#23272F' } },
  { id: 'underwriter', position: { x: 600, y: 400 }, data: { label: 'underwriter' }, style: { background: '#90caf9', color: '#23272F' } },
  { id: 'actuarial_analyst', position: { x: 720, y: 480 }, data: { label: 'actuarial_analyst' }, style: { background: '#90caf9', color: '#23272F' } },
  { id: 'customer_service_representative', position: { x: 600, y: 260 }, data: { label: 'customer_service_representative' }, style: { background: '#90caf9', color: '#23272F' } },
  { id: 'policy_admin_coordinator', position: { x: 800, y: 180 }, data: { label: 'policy_admin_coordinator' }, style: { background: '#90caf9', color: '#23272F' } },
  { id: 'compliance_officer', position: { x: 920, y: 60 }, data: { label: 'compliance_officer' }, style: { background: '#90caf9', color: '#23272F' } },
];
const insuranceEdges: Edge[] = [
  { id: 'e_lc_ca', source: 'legal_counsel', target: 'claims_adjuster', animated: false },
  { id: 'e_ca_cs', source: 'claims_adjuster', target: 'claims_supervisor', animated: false },
  { id: 'e_cs_scm', source: 'claims_supervisor', target: 'senior_claims_manager', animated: false },
  { id: 'e_ca_csr', source: 'claims_adjuster', target: 'customer_service_representative', animated: false },
  { id: 'e_csr_pac', source: 'customer_service_representative', target: 'policy_admin_coordinator', animated: false },
  { id: 'e_pac_co', source: 'policy_admin_coordinator', target: 'compliance_officer', animated: false },
  { id: 'e_ca_uw', source: 'claims_adjuster', target: 'underwriter', animated: false },
  { id: 'e_uw_aa', source: 'underwriter', target: 'actuarial_analyst', animated: false },
  { id: 'e_uw_rm', source: 'underwriter', target: 'risk_manager', animated: false },
  { id: 'e_rm_scm', source: 'risk_manager', target: 'senior_claims_manager', animated: false },
  { id: 'e_scm_ca', source: 'senior_claims_manager', target: 'claims_adjuster', animated: false },
];

// Suggestions (all 10 for both domains)
const retailSuggestionDetails = [
  { agent: 'Customer Service Rep', focus: 'Receives scenario and coordinates initial response.', needs: 'Details of the customer issue and context.' },
  { agent: 'Product Specialist', focus: 'Reviews product details and requirements.', needs: 'Product specifications and customer requirements.' },
  { agent: 'Warehouse Manager', focus: 'Checks stock and logistics.', needs: 'Current stock levels and shipment schedules.' },
  { agent: 'Inventory Manager', focus: 'Updates inventory records.', needs: 'Inventory database access and transaction logs.' },
  { agent: 'Merchandising Manager', focus: 'Adjusts in-store displays and promotions.', needs: 'Promotion schedules and display plans.' },
  { agent: 'Order Fulfillment Coordinator', focus: 'Prepares order for shipment.', needs: 'Order details and delivery schedules.' },
  { agent: 'Logistics Coordinator', focus: 'Arranges delivery and tracking.', needs: 'Carrier options and tracking systems.' },
  { agent: 'Returns Manager', focus: 'Processes return and updates records.', needs: 'Return authorization and customer feedback.' },
  { agent: 'Ecommerce Manager', focus: 'Updates online listings and notifies customer.', needs: 'Online catalog and customer contact info.' },
  { agent: 'Marketing Manager', focus: 'Sends promotional updates to customer.', needs: 'Current promotions and customer preferences.' },
];
const insuranceSuggestionDetails = [
  { agent: 'Legal Counsel', focus: 'Reviews legal aspects and compliance.', needs: 'Access to policy and claim documents.' },
  { agent: 'Claims Adjuster', focus: 'Evaluates the claim and collects evidence.', needs: 'Claim details and supporting evidence.' },
  { agent: 'Claims Supervisor', focus: 'Oversees claim processing.', needs: 'Status reports and escalation protocols.' },
  { agent: 'Senior Claims Manager', focus: 'Makes final approval or escalation.', needs: 'Summary of findings and recommendations.' },
  { agent: 'Risk Manager', focus: 'Assesses risk and recommends action.', needs: 'Risk assessment tools and historical data.' },
  { agent: 'Underwriter', focus: 'Reviews policy and risk factors.', needs: 'Policy documents and risk profiles.' },
  { agent: 'Actuarial Analyst', focus: 'Provides statistical analysis.', needs: 'Statistical models and claim data.' },
  { agent: 'Customer Service Representative', focus: 'Communicates with the customer.', needs: 'Contact info and communication logs.' },
  { agent: 'Policy Admin Coordinator', focus: 'Updates policy records.', needs: 'Policy management system access.' },
  { agent: 'Compliance Officer', focus: 'Ensures regulatory compliance.', needs: 'Compliance checklists and audit logs.' },
];

// Stepper logic
const retailSequence = [
  'customer_service_rep',
  'product_specialist',
  'warehouse_manager',
  'inventory_manager',
  'merchandising_manager',
  'order_fulfillment_coordinator',
  'logistics_coordinator',
  'returns_manager',
  'ecommerce_manager',
  'marketing_manager',
];
const insuranceSequence = [
  'legal_counsel',
  'claims_adjuster',
  'claims_supervisor',
  'senior_claims_manager',
  'risk_manager',
  'underwriter',
  'actuarial_analyst',
  'customer_service_representative',
  'policy_admin_coordinator',
  'compliance_officer',
];
const retailAgentResponsesDefault: Record<string, string> = {
  customer_service_rep: 'Customer Service Rep: Receives scenario and coordinates initial response.',
  product_specialist: 'Product Specialist: Reviews product details and requirements.',
  warehouse_manager: 'Warehouse Manager: Checks stock and logistics.',
  inventory_manager: 'Inventory Manager: Updates inventory records.',
  merchandising_manager: 'Merchandising Manager: Adjusts in-store displays and promotions.',
  order_fulfillment_coordinator: 'Order Fulfillment Coordinator: Prepares order for shipment.',
  logistics_coordinator: 'Logistics Coordinator: Arranges delivery and tracking.',
  returns_manager: 'Returns Manager: Processes return and updates records.',
  ecommerce_manager: 'Ecommerce Manager: Updates online listings and notifies customer.',
  marketing_manager: 'Marketing Manager: Sends promotional updates to customer.',
};

const retailAgentResponsesOrders: Record<string, string> = {
  customer_service_rep: 'Customer Service Rep: "I have been receiving inquiries about the status of orders. Customers are eager for updates, especially for those delayed. We should ensure that we provide timely information to enhance customer satisfaction.”',
  product_specialist: 'Product Specialist: "I recommend checking the product availability on our inventory system. If certain items are running low, we need to communicate that to the Order Fulfillment Coordinator to manage customer expectations properly.”',
  warehouse_manager: 'Warehouse Manager: "Currently, the warehouse is efficiently handling orders, but we have seen an increase in order volume. We need to optimize our picking and packing processes to maintain speedy deliveries.”',
  inventory_manager: "Inventory Manager: \"It's crucial to regularly review our inventory levels to avoid stockouts. I suggest running an inventory report to ensure we have sufficient stock for upcoming orders.\"",
  merchandising_manager: 'Merchandising Manager: "We should monitor the trends in customer orders. If specific products are more popular, we may want to adjust our merchandising strategy or promotions accordingly to push those items further.”',
  order_fulfillment_coordinator: 'Order Fulfillment Coordinator: "I am currently prioritizing orders based on delivery dates. Ensuring that we meet or exceed those timelines is my top priority, and I am coordinating with our logistics team to ensure smooth delivery.”',
  logistics_coordinator: 'Logistics Coordinator: "I am working closely with shipping partners to ensure that all packages are dispatched on time. We need to anticipate any potential delays in the supply chain and communicate these proactively to the Order Fulfillment Coordinator.”',
  returns_manager: 'Returns Manager: "I suggest looking into the reasons for returns related to the current orders. Understanding common issues will help improve our product offerings and order processing systems.”',
  ecommerce_manager: 'Ecommerce Manager: "We should analyze the online sales data to see how the current order status aligns with our eCommerce performance metrics. If we notice any drop-offs in customer purchasing during order processing, we need to investigate further.”',
  marketing_manager: 'Marketing Manager: "Once we have an accurate status on orders and processing, we can create targeted marketing campaigns to promote bestselling items and inform customers about new arrivals, enhancing overall sales.”',
};
const insuranceAgentResponses: Record<string, string> = {
  legal_counsel: 'Legal Counsel: Reviews legal aspects and compliance.',
  claims_adjuster: 'Claims Adjuster: Evaluates the claim and collects evidence.',
  claims_supervisor: 'Claims Supervisor: Oversees claim processing.',
  senior_claims_manager: 'Senior Claims Manager: Makes final approval or escalation.',
  risk_manager: 'Risk Manager: Assesses risk and recommends action.',
  underwriter: 'Underwriter: Reviews policy and risk factors.',
  actuarial_analyst: 'Actuarial Analyst: Provides statistical analysis.',
  customer_service_representative: 'Customer Service Rep: Communicates with the customer.',
  policy_admin_coordinator: 'Policy Admin Coordinator: Updates policy records.',
  compliance_officer: 'Compliance Officer: Ensures regulatory compliance.',
};

const steps = 10;

function App() {
  const [domain, setDomain] = useState<'retail' | 'insurance'>('retail');
  const [scenario, setScenario] = useState<string>('');
  const [step, setStep] = useState<number>(1);
  const [agentAnswers, setAgentAnswers] = useState<Record<string, string>>({});
  const [selectedScenario, setSelectedScenario] = useState<string>('');
  const [inputDemo, setInputDemo] = useState<string>('');

  const demoQuestions = domain === 'retail' ? retailDemoQuestions : insuranceDemoQuestions;
  const nodes = domain === 'retail' ? retailNodes : insuranceNodes;
  const edges = domain === 'retail' ? retailEdges : insuranceEdges;
  const sequence = domain === 'retail' ? retailSequence : insuranceSequence;
  const suggestionDetails = domain === 'retail' ? retailSuggestionDetails : insuranceSuggestionDetails;

  // Fetch agent answers from FastAPI backend
  const fetchAgentAnswers = async (domain: string, scenario: string) => {
    if (!scenario.trim()) {
      setAgentAnswers({});
      return;
    }
    try {
      const res = await fetch(`http://127.0.0.1:8080/agent-answers?domain=${domain}&scenario=${encodeURIComponent(scenario)}`);
      const data = await res.json();
      setAgentAnswers(data.answers || {});
    } catch (err) {
      setAgentAnswers({});
    }
  };



  // Reset all scenario-related state when domain changes
  useEffect(() => {
    setScenario('');
    setSelectedScenario('');
    setAgentAnswers({});
    setStep(1);
    setInputDemo('');
  }, [domain]);

  // Highlight the current agent in the sequence
  const getStepNodes = () => {
    return nodes.map(node =>
      node.id === sequence[step - 1]
        ? { ...node, style: { ...node.style, background: '#ef5350', color: '#fff' } }
        : { ...node, style: { ...node.style, background: '#90caf9', color: '#23272F' } }
    );
  };

  const handleDomainChange = (newDomain: 'retail' | 'insurance') => {
    setDomain(newDomain);
    setScenario('');
    setStep(1);
  };

  const handleScenarioSubmit = () => {
    setStep(1);
    fetchAgentAnswers(domain, scenario);
    setSelectedScenario(scenario);
    setScenario('');
    setInputDemo('');
  };


  const handleNextStep = () => {
    if (step < sequence.length) setStep(step + 1);
  };

  const handleRestart = () => {
    setStep(1);
  };

  // Get current agent's response
  const getCurrentAgentResponse = () => {
    const agentId = sequence[step - 1];
    return agentAnswers[agentId] || '';
  };


  return (
    <div style={{ background: '#181B23', minHeight: '100vh', color: '#fff', fontFamily: 'Inter, Arial, sans-serif' }}>
      <Sidebar domain={domain} onDomainChange={handleDomainChange} />
      <div style={{ marginLeft: 100, padding: 32 }}>
        <h1 style={{
          color: '#C6FF00',
          fontWeight: 'bold',
          fontSize: '2.1rem',
          letterSpacing: 1,
          marginBottom: 18,
          textShadow: '0 2px 10px #23272F',
        }}>
          Agentic AI {domain === 'retail' ? 'Retail' : 'Insurance'} Optimization
          <span style={{ color: '#fff', fontWeight: 400, fontSize: '1.1rem', marginLeft: 8, letterSpacing: 0, textShadow: 'none' }}>
            – Multi-Agent Network
          </span>
        </h1>
        <ScenarioInputBar
          scenario={scenario}
          setScenario={setScenario}
          demoQuestions={demoQuestions}
          onSubmit={handleScenarioSubmit}
          selectedDemo={inputDemo}
          setSelectedDemo={setInputDemo}
        />
        {(() => {
          if (!selectedScenario) return null;
          const allAnswers = Object.values(agentAnswers);
          const uniqueAnswers = Array.from(new Set(allAnswers.filter(Boolean)));
          const fallbackMsg = "I am currently running locally with FastAPI DB. Once I am integrated with AI Foundry, I will be able to answer everything.";
          const quantitativeResponses = [
            "Last month, our total sales reached $150,000, showing a significant increase compared to previous months.",
            "Last month’s sales increased by 20% compared to the same month last year, where total sales were $125,000. This shows strong growth year-over-year.",
            "Our total revenue for last month was $180,000, factoring in both sales and any additional income streams. This represents an increase from $150,000 in revenue during the same period last year.",
            "The top-selling products last month were:\nCozyNights Sleeping Bag: 1,200 units sold\nTrailMaster X4 Tent: 850 units sold\nTrekReady Hiking Boots: 600 units sold",
            "The CozyNights Sleeping Bag generated $60,000 in revenue last month, making it our highest-earning product. Each unit sold for $50.",
            "Last year, we sold 600 units of the TrailMaster X4 Tent in the same month, indicating a substantial growth in sales this year with 850 units sold.",
            "With current trends and customer interest, we project a 15% increase in sales for this month, aiming for $172,500 in total sales.",
            "We should analyze customer feedback and sales data for underperforming products such as the TrekStar Hiking Sandals, which sold only 150 units last month. Strategies may include promotional discounts, enhanced marketing efforts, or product bundling.",
            "Last month, we processed $5,000 in returns, which is approximately 3.3% of total sales. Monitoring the reasons for returns will be crucial to reducing this figure in the future.",
            "Strategies may include launching limited-time promotions on best-selling products, enhancing online marketing efforts, and introducing new products that align with customer interests as identified through market research."
          ];
          const basicResponses = [
            "Hello! How can I assist you today?",
            "I'm an AI assistant that can answer scenario-based questions for retail and insurance domains, provide agent-specific suggestions, and help you explore multi-agent workflows.",
            "I'm an AI multi-agent dashboard assistant designed to help with retail and insurance optimization. Ask me anything about those domains!",
            fallbackMsg,
            ...quantitativeResponses
          ];
          if (uniqueAnswers.length === 1 && basicResponses.includes(uniqueAnswers[0])) {
            return null;
          }
          return (
            <div style={{ color: '#fffde7', background: '#23272F', borderRadius: 8, padding: '10px 18px', margin: '8px 0 18px 0', fontWeight: 'bold', fontSize: '1.08rem', textAlign: 'center' }}>
              Currently viewing scenario: <span style={{ color: '#C6FF00' }}>{selectedScenario}</span>
            </div>
          );
        })()}

        {/* Agent Suggestions always shown at top */}
        <div style={{
          background: '#23272F',
          borderRadius: 16,
          padding: 24,
          marginBottom: 24,
        }}>
          {(() => {
            // Detect if all agent answers are identical and match a known basic_ai_responses value
            const allAnswers = Object.values(agentAnswers);
            const uniqueAnswers = Array.from(new Set(allAnswers.filter(Boolean)));
            // List of known basic responses (keep in sync with backend)
            const fallbackMsg = "I am currently running locally with FastAPI DB. Once I am integrated with AI Foundry, I will be able to answer everything.";
            const quantitativeResponses = [
              "Last month, our total sales reached $150,000, showing a significant increase compared to previous months.",
              "Last month’s sales increased by 20% compared to the same month last year, where total sales were $125,000. This shows strong growth year-over-year.",
              "Our total revenue for last month was $180,000, factoring in both sales and any additional income streams. This represents an increase from $150,000 in revenue during the same period last year.",
              "The top-selling products last month were:\nCozyNights Sleeping Bag: 1,200 units sold\nTrailMaster X4 Tent: 850 units sold\nTrekReady Hiking Boots: 600 units sold",
              "The CozyNights Sleeping Bag generated $60,000 in revenue last month, making it our highest-earning product. Each unit sold for $50.",
              "Last year, we sold 600 units of the TrailMaster X4 Tent in the same month, indicating a substantial growth in sales this year with 850 units sold.",
              "With current trends and customer interest, we project a 15% increase in sales for this month, aiming for $172,500 in total sales.",
              "We should analyze customer feedback and sales data for underperforming products such as the TrekStar Hiking Sandals, which sold only 150 units last month. Strategies may include promotional discounts, enhanced marketing efforts, or product bundling.",
              "Last month, we processed $5,000 in returns, which is approximately 3.3% of total sales. Monitoring the reasons for returns will be crucial to reducing this figure in the future.",
              "Strategies may include launching limited-time promotions on best-selling products, enhancing online marketing efforts, and introducing new products that align with customer interests as identified through market research."
            ];
            const basicResponses = [
              "Hello! How can I assist you today?",
              "I'm an AI assistant that can answer scenario-based questions for retail and insurance domains, provide agent-specific suggestions, and help you explore multi-agent workflows.",
              "I'm an AI multi-agent dashboard assistant designed to help with retail and insurance optimization. Ask me anything about those domains!",
              fallbackMsg,
              ...quantitativeResponses
            ];
            if (selectedScenario && uniqueAnswers.length === 1 && basicResponses.includes(uniqueAnswers[0])) {
              return (
                <div style={{ textAlign: 'center', marginTop: 40 }}>
                  <h2 style={{ color: '#C6FF00', fontWeight: 'bold', fontSize: '1.4rem', marginBottom: 24 }}>Agent Response</h2>
                  <div style={{ color: '#C6FF00', fontWeight: 'bold', fontSize: '1.4rem', whiteSpace: 'pre-line' }}>{uniqueAnswers[0]}</div>
                </div>
              );
            }
            if (selectedScenario) {
              return (
                <>
                  <h2 style={{ color: '#C6FF00', fontWeight: 'bold', fontSize: '1.4rem', marginBottom: 12 }}>
                    Agent Suggestions
                  </h2>
                  <ul style={{ color: '#fff', fontSize: '1.1rem', listStyle: 'none', padding: 0 }}>
                    {sequence.map((agentId, i) => (
                      <li key={i} style={{ marginBottom: 24 }}>
                        <div style={{ color: '#C6FF00', fontWeight: 'bold', fontSize: '1.15rem' }}>{agentId.replace(/_/g, ' ').replace(/\b\w/g, c => c.toUpperCase())}:</div>
                        <div>{agentAnswers[agentId] || <span style={{ color: '#888' }}>No answer available.</span>}</div>
                      </li>
                    ))}
                  </ul>
                </>
              );
            }
            return (
              <div style={{ color: '#fff', fontSize: '1.1rem', opacity: 0.7, textAlign: 'center' }}>
                No scenario asked. Please enter a question above.
              </div>
            );
          })()}

        </div>
        {/* Stepper and Network always shown, but with message if no scenario */}
        <div style={{ background: '#23272F', borderRadius: 16, padding: 24, marginBottom: 24 }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 8 }}>
            <span style={{ color: '#fff' }}>Step {step} of {steps}</span>
            {step < sequence.length ? (
              <button
                style={{ background: '#FFC107', color: '#23272F', fontWeight: 'bold', border: 'none', borderRadius: 8, padding: '8px 28px', fontSize: '1.1rem', cursor: 'pointer' }}
                onClick={handleNextStep}
              >
                Next
              </button>
            ) : (
              <button
                style={{ background: '#FFC107', color: '#23272F', fontWeight: 'bold', border: 'none', borderRadius: 8, padding: '8px 28px', fontSize: '1.1rem', cursor: 'pointer' }}
                onClick={handleRestart}
              >
                Restart
              </button>
            )}
          </div>
          <AgentNetwork nodes={getStepNodes()} edges={edges} />
        </div>
        {/* Agent Response and Suggestion always shown, but with message if no scenario */}
        <div style={{ background: '#23272F', borderRadius: 16, padding: 24, minHeight: 60, color: '#fff', fontSize: '1.1rem' }}>
          {(() => {
            const allAnswers = Object.values(agentAnswers);
            const uniqueAnswers = Array.from(new Set(allAnswers.filter(Boolean)));
            const fallbackMsg = "I am currently running locally with FastAPI DB. Once I am integrated with AI Foundry, I will be able to answer everything.";
            const basicResponses = [
              "Hello! How can I assist you today?",
              "I'm an AI assistant that can answer scenario-based questions for retail and insurance domains, provide agent-specific suggestions, and help you explore multi-agent workflows.",
              "I'm an AI multi-agent dashboard assistant designed to help with retail and insurance optimization. Ask me anything about those domains!",
              fallbackMsg
            ];
            if (selectedScenario && uniqueAnswers.length === 1 && basicResponses.includes(uniqueAnswers[0])) {
              return null;
            }
            if (selectedScenario) {
              return (
                <div>
                  <div style={{ fontWeight: 'bold', color: '#fffde7', background: '#222', padding: '6px 12px', borderRadius: 6, marginBottom: 12, display: 'inline-block' }}>
                    {agentAnswers[sequence[step - 1]] || <span style={{ color: '#888' }}>No answer available.</span>}
                  </div>
                  <div style={{ marginTop: 16 }}>
                    {(() => {
                      const currentAgent = sequence[step - 1];
                      const suggestion = suggestionDetails.find(
                        s => s.agent.replace(/\s+/g, '_').toLowerCase() === currentAgent
                      );
                      return suggestion ? (
                        <div style={{ color: '#C6FF00', background: '#161b22', borderRadius: 6, padding: '10px 18px', marginTop: 8 }}>
                          <div><b>Focus:</b> <span style={{ color: '#fff' }}>{suggestion.focus}</span></div>
                          <div><b>Needs:</b> <span style={{ color: '#fff' }}>{suggestion.needs}</span></div>
                        </div>
                      ) : null;
                    })()}
                  </div>
                </div>
              );
            }
            return null;
          })()}

        </div>

      </div>
    </div>
  );
}

export default App;