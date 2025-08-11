from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow CORS for local frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For dev, restrict in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Example data structure for insurance scenarios
insurance_agent_answers = {
    "A customer has submitted a complex claim involving multiple policies and potential fraud indicators. How should we proceed?": {
        "legal_counsel": "We should first review the legal implications of the claim and ensure all documentation complies with regulatory standards. If fraud is suspected, we may need to involve external counsel or law enforcement.",
        "claims_adjuster": "I'll begin by verifying the claim details, inspecting any physical evidence, and assessing the estimated loss. I’ll flag any inconsistencies for further review.",
        "claims_supervisor": "Let’s ensure the adjuster has all necessary resources and escalate the case to senior management if thresholds are exceeded. I’ll also coordinate with underwriting for policy overlap.",
        "senior_claims_manager": "We need a cross-functional review involving legal, underwriting, and compliance. I’ll initiate a case audit and ensure the customer is kept informed throughout.",
        "risk_manager": "This case presents elevated risk. I’ll evaluate exposure across policies and recommend mitigation steps, including potential policy revisions or premium adjustments.",
        "underwriter": "I'll assess whether the policies were correctly underwritten and if any exclusions apply. This may also prompt a review of underwriting guidelines for similar cases.",
        "actuarial_analyst": "I’ll analyze the financial impact and probability of similar claims. This data will help inform future pricing and risk models.",
        "customer_service_rep": "I’ll ensure the customer receives timely updates and support. I’ll also gather any missing documents and clarify next steps to maintain trust.",
        "policy_admin_coordinator": "I’ll verify policy details, coverage limits, and ensure all relevant policies are linked correctly in the system for accurate processing.",
        "compliance_officer": "I’ll review the claim against internal policies and external regulations. If fraud indicators are present, I’ll initiate a compliance investigation and report findings."
    },

    "What steps are involved in processing a new insurance claim?": {
        "claims_adjuster": "First, I review the submitted claim and supporting documents for completeness. Then I contact the policyholder if additional information is needed and initiate the investigation process.",
        "underwriter": "I assess the risk factors associated with the claim and verify that the policy covers the reported incident. I may consult with the actuary for complex or high-value claims.",
        "customer_service_rep": "I guide the policyholder through the claim submission process and provide status updates. I also answer any questions they have about required documentation or timelines.",
        "fraud_investigator": "If there are any red flags or anomalies in the claim, I conduct a deeper investigation to rule out potential fraud before the claim is approved.",
        "actuary": "I provide statistical analysis and loss projections to help determine the appropriate payout amount for the claim, based on historical data and risk models.",
        "claims_manager": "I oversee the entire claims process, ensure compliance with regulations, and approve final payouts. I also coordinate with other departments to resolve escalated or complex cases."
    },

    "What percentage of claims this quarter were approved versus denied?": {
        "claims_adjuster": "Out of 1,200 claims processed this quarter, 900 (75%) were approved and 300 (25%) were denied. Most denials were due to incomplete documentation or policy exclusions.",
        "underwriter": "The approval rate of 75% aligns with our risk models. Of the denied claims, 60% were flagged as high-risk or outside policy scope.",
        "customer_service_rep": "We received 1,200 claim inquiries and resolved 1,050 (87.5%) within the standard 3-day response time. 150 cases required escalation due to complex issues.",
        "fraud_investigator": "Of the 300 denied claims, 45 were flagged for potential fraud, representing 3.75% of all claims this quarter.",
        "actuary": "Our projected claims approval rate was 72%, so the actual 75% is favorable and reduces our expected payout variance by $120,000.",
        "claims_manager": "We saw a 10% increase in total claims compared to last quarter. The average claim payout was $4,200, totaling $3.78 million in approved payouts."
    },
    "How many new policies were sold this month and what is the average premium?": {
        "sales_agent": "We sold 340 new policies this month. The average premium per policy was $1,150, with the highest segment being auto insurance (150 policies).",
        "underwriter": "Of the 340 new policies, 90 were for high-risk clients, requiring additional review. The average premium for high-risk policies was $1,800.",
        "customer_service_rep": "We fielded 520 inquiries about new policies and successfully converted 65% into sales. Most questions were about coverage limits and deductibles.",
        "actuary": "The total premium collected from new policies this month is $391,000. This is a 7% increase over last month’s new business.",
        "policy_admin": "All new policies have been issued and 98% of customers received their documents within 24 hours. Only 2 policies are pending due to missing client information.",
        "marketing_manager": "Our targeted campaign for life insurance resulted in 60 new policies, a 20% conversion rate from 300 leads."
    },
    "What is the current claim turnaround time and how does it compare to last quarter?": {
        "claims_adjuster": "The average claim turnaround time this quarter is 4.2 days, down from 5.1 days last quarter. 68% of claims were resolved within 3 days.",
        "claims_manager": "Turnaround time improved by 18%. Fast-track claims (under $2,000) averaged 2.1 days, while complex claims averaged 7.8 days.",
        "customer_service_rep": "We received positive feedback from 92% of customers whose claims were resolved within 3 days. Only 4% reported dissatisfaction with claim speed.",
        "actuary": "This reduction in turnaround time is expected to lower customer churn by 2% and improve our net promoter score by 4 points.",
        "fraud_investigator": "Expedited claims are monitored for fraud. Out of 820 expedited claims, only 2 were flagged for further review."
    },
    "How many policies lapsed this month and what is the retention rate?": {
        "policy_admin": "Out of 2,500 active policies, 120 lapsed this month (4.8%). 2,380 policies were renewed, giving us a retention rate of 95.2%.",
        "customer_service_rep": "We contacted all policyholders with pending lapses. Of 150 contacted, 30 reinstated their policies after a reminder call.",
        "marketing_manager": "Our retention campaign contributed to a 1.5% improvement in retention compared to last month. Email reminders had a 45% open rate.",
        "underwriter": "Most lapses occurred in the auto segment, with 80 out of 120 lapses. The main reason cited was premium affordability.",
        "actuary": "The lapse rate is within our forecasted range. The financial impact is a $138,000 reduction in annual premium revenue."
    },
    "What is the average claim payout for property damage versus personal injury?": {
        "claims_adjuster": "The average payout for property damage claims is $5,800, while personal injury claims average $14,200.",
        "claims_manager": "Property damage claims made up 62% of all claims, but personal injury claims accounted for 71% of total payout dollars.",
        "actuary": "Total payout for property damage this quarter was $2.9 million; for personal injury, it was $5.1 million.",
        "fraud_investigator": "Personal injury claims are 2.6 times more likely to be flagged for fraud. 12 cases were referred for investigation this quarter.",
        "underwriter": "We are reviewing underwriting guidelines for personal injury coverage to manage the higher average payouts."
    },
    "What percentage of claims this quarter were approved versus denied?": {
        "claims_adjuster": "Out of 1,200 claims processed this quarter, 900 (75%) were approved and 300 (25%) were denied. Most denials were due to incomplete documentation or policy exclusions.",
        "underwriter": "The approval rate of 75% aligns with our risk models. Of the denied claims, 60% were flagged as high-risk or outside policy scope.",
        "customer_service_rep": "We received 1,200 claim inquiries and resolved 1,050 (87.5%) within the standard 3-day response time. 150 cases required escalation due to complex issues.",
        "fraud_investigator": "Of the 300 denied claims, 45 were flagged for potential fraud, representing 3.75% of all claims this quarter.",
        "actuary": "Our projected claims approval rate was 72%, so the actual 75% is favorable and reduces our expected payout variance by $120,000.",
        "claims_manager": "We saw a 10% increase in total claims compared to last quarter. The average claim payout was $4,200, totaling $3.78 million in approved payouts."
    },
    "How many new policies were sold this month and what is the average premium?": {
        "sales_agent": "We sold 340 new policies this month. The average premium per policy was $1,150, with the highest segment being auto insurance (150 policies).",
        "underwriter": "Of the 340 new policies, 90 were for high-risk clients, requiring additional review. The average premium for high-risk policies was $1,800.",
        "customer_service_rep": "We fielded 520 inquiries about new policies and successfully converted 65% into sales. Most questions were about coverage limits and deductibles.",
        "actuary": "The total premium collected from new policies this month is $391,000. This is a 7% increase over last month’s new business.",
        "policy_admin": "All new policies have been issued and 98% of customers received their documents within 24 hours. Only 2 policies are pending due to missing client information.",
        "marketing_manager": "Our targeted campaign for life insurance resulted in 60 new policies, a 20% conversion rate from 300 leads."
    },
    "What is the current claim turnaround time and how does it compare to last quarter?": {
        "claims_adjuster": "The average claim turnaround time this quarter is 4.2 days, down from 5.1 days last quarter. 68% of claims were resolved within 3 days.",
        "claims_manager": "Turnaround time improved by 18%. Fast-track claims (under $2,000) averaged 2.1 days, while complex claims averaged 7.8 days.",
        "customer_service_rep": "We received positive feedback from 92% of customers whose claims were resolved within 3 days. Only 4% reported dissatisfaction with claim speed.",
        "actuary": "This reduction in turnaround time is expected to lower customer churn by 2% and improve our net promoter score by 4 points.",
        "fraud_investigator": "Expedited claims are monitored for fraud. Out of 820 expedited claims, only 2 were flagged for further review."
    },
    "How many policies lapsed this month and what is the retention rate?": {
        "policy_admin": "Out of 2,500 active policies, 120 lapsed this month (4.8%). 2,380 policies were renewed, giving us a retention rate of 95.2%.",
        "customer_service_rep": "We contacted all policyholders with pending lapses. Of 150 contacted, 30 reinstated their policies after a reminder call.",
        "marketing_manager": "Our retention campaign contributed to a 1.5% improvement in retention compared to last month. Email reminders had a 45% open rate.",
        "underwriter": "Most lapses occurred in the auto segment, with 80 out of 120 lapses. The main reason cited was premium affordability.",
        "actuary": "The lapse rate is within our forecasted range. The financial impact is a $138,000 reduction in annual premium revenue."
    },
    "What is the average claim payout for property damage versus personal injury?": {
        "claims_adjuster": "The average payout for property damage claims is $5,800, while personal injury claims average $14,200.",
        "claims_manager": "Property damage claims made up 62% of all claims, but personal injury claims accounted for 71% of total payout dollars.",
        "actuary": "Total payout for property damage this quarter was $2.9 million; for personal injury, it was $5.1 million.",
        "fraud_investigator": "Personal injury claims are 2.6 times more likely to be flagged for fraud. 12 cases were referred for investigation this quarter.",
        "underwriter": "We are reviewing underwriting guidelines for personal injury coverage to manage the higher average payouts."
    }
}

# Example data structure for retail scenarios
retail_agent_answers = {
    "What is the current status of customer orders, and how are we processing them?": {
        "customer_service_rep": "I have been receiving inquiries about the status of orders. Customers are eager for updates, especially for those delayed. We should ensure that we provide timely information to enhance customer satisfaction.",
        "product_specialist": "I recommend checking the product availability on our inventory system. If certain items are running low, we need to communicate that to the Order Fulfillment Coordinator to manage customer expectations properly.",
        "warehouse_manager": "Currently, the warehouse is efficiently handling orders, but we have seen an increase in order volume. We need to optimize our picking and packing processes to maintain speedy deliveries.",
        "inventory_manager": "It's crucial to regularly review our inventory levels to avoid stockouts. I suggest running an inventory report to ensure we have sufficient stock for upcoming orders.",
        "merchandising_manager": "We should monitor the trends in customer orders. If specific products are more popular, we may want to adjust our merchandising strategy or promotions accordingly to push those items further.",
        "order_fulfillment_coordinator": "I am currently prioritizing orders based on delivery dates. Ensuring that we meet or exceed those timelines is my top priority, and I am coordinating with our logistics team to ensure smooth delivery.",
        "logistics_coordinator": "I am working closely with shipping partners to ensure that all packages are dispatched on time. We need to anticipate any potential delays in the supply chain and communicate these proactively to the Order Fulfillment Coordinator.",
        "returns_manager": "I suggest looking into the reasons for returns related to the current orders. Understanding common issues will help improve our product offerings and order processing systems.",
        "ecommerce_manager": "We should analyze the online sales data to see how the current order status aligns with our eCommerce performance metrics. If we notice any drop-offs in customer purchasing during order processing, we need to investigate further.",
        "marketing_manager": "Once we have an accurate status on orders and processing, we can create targeted marketing campaigns to promote bestselling items and inform customers about new arrivals, enhancing overall sales."
    },
    "Are there any pending orders that require immediate attention or resolution?": {
        "customer_service_rep": "Yes, I've noted several customer inquiries about pending orders. We need to prioritize communication with those customers to reassure them that their orders are being handled and provide them with updates.",
        "product_specialist": "We should review the list of pending orders to identify if any items are out of stock. This will allow us to address any specific products that may need reordering or restocking immediately.",
        "warehouse_manager": "There are a few pending orders that are waiting on specific items. I recommend a review of our picking status and assigning additional workforce to help expedite these orders in the warehouse.",
        "inventory_manager": "I will assist by checking our inventory levels for any items related to these pending orders. If there are discrepancies, we need to resolve these quickly to fulfill outstanding requests.",
        "merchandising_manager": "We should evaluate any pending orders to understand the demand for certain products. If items are consistently delayed, it may indicate that we need to adjust our inventory strategy for those products.",
        "order_fulfillment_coordinator": "I have identified some pending orders that are approaching their due dates. I will prioritize these in our fulfillment queue and coordinate with the warehouse to expedite their processing.",
        "logistics_coordinator": "I'll check the status of shipments for all pending orders. If there are any delays in logistics or shipping, we need to escalate these issues immediately to get them resolved.",
        "returns_manager": "If there are pending orders due to customer returns or exchanges, we must process those swiftly. Assessing these returns will help us avoid further delays in fulfilling new orders.",
        "ecommerce_manager": "It’s important to track the conversion rates for pending orders on our online platform. If customers abandon their carts or check out but don't complete the order, we need to understand why and address any barriers.",
        "marketing_manager": "Once we’ve resolved any immediate issues with pending orders, we can use targeted marketing strategies to promote those items and encourage new orders. This might also include special promotions for the items that are in high demand."
    },
    "What trends do we see in recent sales data, and which products are performing well?": {
        "customer_service_rep": "I have observed an increase in queries about the CozyNights Sleeping Bag and TrailMaster X4 Tent. Customers are particularly interested in their availability, as they seem to be highly sought after based on recent requests.",
        "product_specialist": "The data shows that the CozyNights Sleeping Bag is performing exceptionally well, particularly among campers. Its lightweight and compact design is a major selling point. Additionally, the TrailMaster X4 Tent has gained attention due to its spacious interior and durability.",
        "warehouse_manager": "We need to ensure that we have adequate stock levels of the most popular items like the CozyNights Sleeping Bag and TrailMaster X4 Tent. They are selling quickly, and we should prioritize restocking these products in our warehouse.",
        "inventory_manager": "I recommend closely monitoring the sales patterns for these top-performing products. We should analyze the purchasing frequency and adjust our inventory orders accordingly to prevent stockouts, especially for the items that have high sales velocity.",
        "merchandising_manager": "The trends suggest that products with excellent customer reviews, such as the CozyNights Sleeping Bag, are driving sales. We should highlight these products in our merchandising efforts and consider bundling items to enhance sales further.",
        "order_fulfillment_coordinator": "There have been a few large orders coming in for the CozyNights Sleeping Bag and TrailMaster X4 Tent over the last month. Ensuring these orders are prioritized will help us maintain customer satisfaction and encourage repeat business.",
        "logistics_coordinator": "I have noticed that shipping for the TrailMaster X4 Tent has increased. We must coordinate logistics to ensure we can handle larger shipments efficiently, especially as we anticipate higher demand in the coming months.",
        "returns_manager": "Monitoring the return rates for these trending products is crucial. If we notice spikes in returns for the CozyNights Sleeping Bag, we should investigate common issues that customers are facing regarding comfort or fitting.",
        "ecommerce_manager": "Data from our eCommerce platform indicates that the TrailMaster X4 Tent and CozyNights Sleeping Bag are the most frequently purchased items recently. We should consider promotional campaigns to leverage this popularity and boost visibility for these items.",
        "marketing_manager": "I suggest we create targeted marketing campaigns around the trends we are witnessing with the CozyNights Sleeping Bag and the TrailMaster X4 Tent. Highlighting customer testimonials and success stories can resonate well with potential buyers, driving even more sales."
    },
    "What are the current stock levels for our top-selling products?": {
        "customer_service_rep": "We've received multiple inquiries about stock levels, particularly for the CozyNights Sleeping Bag and TrailMaster X4 Tent. Ensuring these products are in stock is crucial as they are popular among our customers.",
        "product_specialist": "Based on our data, the top-selling products are the CozyNights Sleeping Bag, TrailMaster X4 Tent, and TrekReady Hiking Boots. We need to maintain stock levels for these items to meet demand effectively.",
        "warehouse_manager": "Currently, we have the following stock levels:\nCozyNights Sleeping Bag: 100 units\nTrailMaster X4 Tent: 75 units\nTrekReady Hiking Boots: 50 units\nWe are close to the reorder point for the TrekReady Hiking Boots, and I recommend placing a restock order soon.",
        "inventory_manager": "I've analyzed the stock levels and compare them to recent sales trends. Given that the CozyNights Sleeping Bag is among our bestsellers, we need to ensure we have enough to maintain a buffer stock as sales continue to rise.",
        "merchandising_manager": "These products should be prominently displayed both online and in-store, especially the CozyNights Sleeping Bag and TrailMaster X4 Tent, which have a steady sales momentum. Having strong stock levels will help us capitalize on seasonal promotions.",
        "order_fulfillment_coordinator": "I’ve flagged the inventory for the CozyNights Sleeping Bag as a priority for fulfillment, as we’ve received several large orders recently. Confirming the stock levels with the Warehouse Manager is essential to avoid delays.",
        "logistics_coordinator": "To ensure timely restocking, I’m coordinating with our suppliers for the TrailMaster X4 Tent and TrekReady Hiking Boots. If the current levels drop too low, we might face delays in fulfilling e-commerce orders.",
        "returns_manager": "I will monitor the return rates for these top-selling products. If we see high return rates for the TrekReady Hiking Boots, it may indicate sizing issues or quality concerns that we need to address immediately.",
        "ecommerce_manager": "Our eCommerce platform shows sustained interest in the CozyNights Sleeping Bag and TrailMaster X4 Tent. Given their performance, we should consider restocking these items before the camping season peaks.",
        "marketing_manager": "Once we confirm satisfactory stock levels, we can ramp up marketing initiatives for the CozyNights Sleeping Bag and TrailMaster X4 Tent with summer camping promotions, leveraging the strong sales data we have."
    },
    "When should we reorder specific items to maintain optimal inventory?": {
        "customer_service_rep": "We have had a significant number of inquiries about the CozyNights Sleeping Bag and TrailMaster X4 Tent. It's important that we reorder these items before we exceed our safety stock levels to prevent customer dissatisfaction.",
        "product_specialist": "Based on current sales trends, I suggest we set a reorder point for the CozyNights Sleeping Bag at 50 units, as it's a popular item for all seasons, and for the TrailMaster X4 Tent, we should aim to reorder when we reach 40 units. This should help us stay ahead of customer demand.",
        "warehouse_manager": "I recommend we review our inventory levels and place orders when products drop below 60% of their stock capacity. Currently, our stock levels for key items are:\nCozyNights Sleeping Bag: 100 units\nTrailMaster X4 Tent: 75 units\nTrekReady Hiking Boots: 50 units\nWe could reorder the TrekReady Hiking Boots now, as they're nearing our minimum levels.",
        "inventory_manager": "I will keep an eye on turnover rates for our top-selling items. We should aim for a reorder every four weeks for the CozyNights Sleeping Bag and every six weeks for the TrekReady Hiking Boots, assuming consistent sales rates.",
        "merchandising_manager": "If we see sales trending upward for the TrailBlaze Hiking Pants as well, we should consider adding them to our reorder list, especially if current stock levels drop below 30 units, as they may become increasingly popular with the warm season approaching.",
        "order_fulfillment_coordinator": "I will prioritize reorders based on pending orders and recent sales volumes. Currently, many customers are waiting for their CozyNights Sleeping Bags. I will make sure our reordering process is aligned with fulfilling those orders as quickly as possible.",
        "logistics_coordinator": "Coordinating with suppliers, I suggest we generate our reorder list two weeks before we anticipate reaching our stock thresholds. This will give us enough lead time to replenish our inventory without delays, especially for popular items like the EcoFire Camping Stove.",
        "returns_manager": "Monitoring the return rates for the CozyNights Sleeping Bag is essential. If we see that several customers are returning these items, we may need to assess whether we should adjust how often we reorder or if we need to correct any underlying issues.",
        "ecommerce_manager": "Given the increased online interactions with our top-selling products, we should automate our inventory management system to trigger reorder alerts when stock falls below specified levels, ensuring we can respond to customer demand efficiently.",
        "marketing_manager": "After we ensure that inventory levels are sufficient, I suggest we time marketing campaigns for our bestsellers right before peak demand seasons, ideally replenishing stock a month prior to that. It’s crucial to align our promotional activities with inventory availability."
    },
    "Are there any products that consistently run low on stock?": {
        "customer_service_rep": "I have noticed that the CozyNights Sleeping Bag frequently runs low on stock due to high customer interest, particularly during the camping season. It's essential to monitor this product closely to meet customer demand.",
        "product_specialist": "The CozyNights Sleeping Bag and TrekReady Hiking Boots are consistently in high demand. We should analyze their sales trends to identify the right time for reordering and avoid stockouts.”",
        "warehouse_manager": "Currently, we are experiencing reduced inventory levels for certain items:\nCozyNights Sleeping Bag: Typically sells out within weeks.\nTrekReady Hiking Boots: Also depletes quickly due to ongoing orders. We need to establish a more consistent restocking schedule to avoid lows.”",
        "inventory_manager": "Both the CozyNights Sleeping Bag and TrekReady Hiking Boots run low often. I suggest adjusting our safety stock levels for these items to ensure we have a buffer, especially before peak seasons.",
        "merchandising_manager": "The ongoing popularity of the CozyNights Sleeping Bag indicates we should increase our promotions and visibility for this product. Keeping sufficient stock will help us capitalize on its popularity.",
        "order_fulfillment_coordinator": "I routinely prioritize orders for the CozyNights Sleeping Bag, as they often have pending orders. Ensuring timely restocking for this item is crucial to fulfilling customer expectations.",
        "logistics_coordinator": "I recommend closely monitoring shipment schedules for the TrekReady Hiking Boots, as they frequently reach low stock levels. We need to coordinate with suppliers for timely restocks.",
        "returns_manager": "We should keep an eye on the return rates for the CozyNights Sleeping Bag. If returns increase, it may affect our stock management and indicate issues we need to address.",
        "ecommerce_manager": "Data indicates a spike in traffic for top-selling products like the CozyNights Sleeping Bag. We must ensure we have enough inventory to handle online demands effectively.",
        "marketing_manager": "To maintain momentum for the CozyNights Sleeping Bag, we should plan marketing initiatives around the times we receive new stock, reinforcing demand and minimizing stockout periods."
    },
    "Are there any unresolved customer issues that need attention?": {
        "customer_service_rep": "There are several unresolved customer issues, primarily related to delayed deliveries of the CozyNights Sleeping Bag. Customers have reached out for updates, and I recommend we prioritize these inquiries.",
        "product_specialist": "I’ve noticed complaints concerning the TrekReady Hiking Boots, specifically regarding fitting issues. It would help to clarify sizing information on the product page to mitigate confusion and improve customer satisfaction.",
        "warehouse_manager": "Currently, we have pending shipping problems for some orders that include the Adventure Dining Table. We need to investigate why these items are delayed in dispatch as it affects customer satisfaction.",
        "inventory_manager": "Some customers have reported receiving incorrect items or missing products from their orders. It’s essential to align our inventory records closely with what is shipped to avoid further discrepancies.",
        "merchandising_manager": "We should analyze the feedback regarding the Summit Breeze Jacket. There are reports of it not performing as expected in certain weather conditions, which we might need to address in our communication about the product.",
        "order_fulfillment_coordinator": "I’ve received multiple alerts about orders containing the EcoFire Camping Stove that haven’t been shipped yet. Addressing these specific cases must be a priority to ensure those customers receive their products promptly.",
        "logistics_coordinator": "There have been issues reported with the shipping carriers regarding delayed deliveries, particularly for orders involving the TrailMaster X4 Tent. We need to reach out for resolution and assess logistics partners.",
        "returns_manager": "I have several returns pending processing, especially associated with the TrekReady Hiking Boots. We must expedite handling these returns to enhance our efficiency and customer trust.",
        "ecommerce_manager": "Customer feedback indicates confusion during the checkout process, particularly related to product availability. We need to enhance our system to provide real-time stock updates.",
        "marketing_manager": "Let’s focus on addressing the concerns around unresolved issues in customer communications. If we can promptly resolve complaints and enhance transparency, it will improve our brand image significantly."
    },
    "What new products should we consider adding based on market demand?": {
        "customer_service_rep": "Customers have been asking for additional camping accessories, especially portable solar chargers and lightweight camping cookware. These items could complement our existing offerings well.",
        "product_specialist": "Based on recent feedback, I recommend adding the EcoFire Camping Stove and TrekStar Hiking Sandals to our product line. Both received positive reviews and would enhance our camping and hiking offerings.",
        "warehouse_manager": "If we do add new products like the Adventurer Pro Backpack – which has a 40L capacity and is designed for rugged adventures – we must ensure we have the appropriate storage space and logistical support for inventory management.",
        "inventory_manager": "We should analyze the turnover rates for existing products. With high demand for durable camping gear, items like the TrekReady TrailWalker Hiking Shoes are also worth considering to expand our footwear options.",
        "merchandising_manager": "Adding products that support eco-friendly outdoor experiences, such as the EcoFire Camping Stove, will resonate with environmentally-conscious consumers and align with current market trends.",
        "order_fulfillment_coordinator": "If we expand to include more categories, like hiking apparel, having a systematic approach for order fulfillment will be vital. For example, introducing the Summit Breeze Jacket, which has been well-received, could boost sales.",
        "logistics_coordinator": "Before adding new products, we need to ensure our logistics can handle the additional complexity. Efficient shipping and handling processes must be established, especially for larger items like the TrailMaster X4 Tent.",
        "returns_manager": "If new products are introduced, it's essential to monitor their return rates closely. Items like the TrekStar Hiking Sandals may require us to look into fitting and sizing options to mitigate returns.",
        "ecommerce_manager": "Market research indicates a growing trend for multifunctional outdoor gear. Products that offer versatility, such as backpacking cooking sets, should be considered for our online catalog.",
        "marketing_manager": "We can create marketing campaigns targeting the eco-friendly angle for products like the EcoFire Camping Stove. Positioning this stove as a must-have for the sustainable camping experience could attract a new customer segment."
    },
    "Are there any delays in shipping that we need to communicate to our customers?": {
        "customer_service_rep": "We've received multiple customer inquiries regarding the delays in shipping for various products, particularly the CozyNights Sleeping Bag and Adventure Dining Table. Customers are eager for updates, and we need to ensure communication is clear.",
        "product_specialist": "Feedback indicates there are shipping delays for the CozyNights Sleeping Bag due to high demand. Customers are concerned about their order status and would benefit from proactive communication regarding expected delivery times.",
        "warehouse_manager": "We are currently facing delays in shipping the Adventure Dining Table due to logistics challenges in sourcing materials. It's crucial to notify customers about these potential delays to manage their expectations.",
        "inventory_manager": "Several top-selling items like the TrekReady Hiking Boots are facing low stock due to unexpected demand; this could affect shipping timelines. I recommend informing customers about potential shipping delays as soon as possible.",
        "merchandising_manager": "It may be beneficial to consider a promotional campaign around our popular items that are currently facing shipping delays. Transparency about these delays will help customers feel informed and valued.",
        "order_fulfillment_coordinator": "I’ve flagged multiple orders containing the CozyNights Sleeping Bag that are delayed in shipping. We must update these customers promptly to avoid frustration.",
        "logistics_coordinator": "We are experiencing delays with certain shipping carriers, particularly for larger items like the TrailMaster X4 Tent. We need to communicate these delays clearly to customers to prevent misunderstandings.",
        "returns_manager": "If any products are delayed due to shipping issues, we should also inform customers about our return policy in light of these delays. This will reassure them that we prioritize customer satisfaction.",
        "ecommerce_manager": "We should update our website and order confirmation emails to reflect any shipping delays. Providing real-time updates can enhance customer trust and reduce support inquiries.",
        "marketing_manager": "Once we have a clearer picture of the shipping delays, we can develop a communication strategy that highlights our commitment to customer service, perhaps through an email campaign that addresses the issue directly."
    },
    "How can we leverage data to understand customer behavior better?": {
        "customer_service_rep": "Tracking customer inquiries and feedback can provide insights into common concerns and preferences. We can analyze this data to adapt our offerings and address issues proactively.",
        "product_specialist": "Utilizing sales data can highlight which products are most popular. By focusing on trending items, we can tailor our inventory and marketing strategies to meet customer demands more effectively.",
        "warehouse_manager": "Implementing a data-driven approach to inventory management can reveal patterns in stock depletion. By understanding when particular products sell out faster, we can better anticipate reorder needs.",
        "inventory_manager": "Analyzing historical sales data will allow us to predict future trends, ensuring that we maintain optimal stock levels of high-demand items. This proactive stance can help minimize stockouts.",
        "merchandising_manager": "We should leverage customer purchase history to create personalized marketing efforts and recommend products based on previous purchases. This kind of targeted approach often increases customer satisfaction and sales.",
        "order_fulfillment_coordinator": "By analyzing the time it takes to fulfill orders, we can identify bottlenecks in our processes. This data allows us to optimize operations and improve delivery times for customers.",
        "logistics_coordinator": "Understanding shipping trends can help us refine our logistics strategy. For instance, we can analyze delays to adjust our shipping partners or methods accordingly, enhancing customer satisfaction.",
        "returns_manager": "By examining return data, we can identify frequently returned items and their reasons. Addressing the root causes can help us improve product quality and reduce return rates.",
        "ecommerce_manager": "Utilizing website analytics will provide insights into customer behavior on our online platform. Studying how customers navigate our site can highlight areas for improvement and boost conversion rates.",
        "marketing_manager": "We can use market research and customer behavior analysis to identify potential new product lines and marketing strategies. Understanding our customer demographics will help tailor our campaigns more effectively."
    }

    # Add more questions/scenarios here as needed
}

 

import re

def normalize_key(key: str) -> str:
    # Lowercase, strip, remove trailing punctuation, collapse whitespace
    return re.sub(r'\s+', ' ', key.strip().lower().rstrip('?.!'))

# Supported basic/general AI questions (not in demo dropdown, but handled if typed):
# - hi
# - hello
# - hey
# - what can you do
# - who are you
# - what is your purpose
# - help
# - what is this
# - what is your name
# - tell me about yourself

basic_ai_responses = [
    (['hi', 'hello', 'hey'], "Hello! How can I assist you today?"),
    (['what can you do', 'what is your purpose', 'help'], "I'm an AI assistant that can answer scenario-based questions for retail and insurance domains, provide agent-specific suggestions, and help you explore multi-agent workflows."),
    (['who are you', 'what is your name', 'tell me about yourself'], "I'm an AI multi-agent dashboard assistant designed to help with retail and insurance optimization. Ask me anything about those domains!")
]

# Supported retail analytics/quantitative questions (not in demo dropdown, but handled if typed):
# - What were the total sales last month?
# - How do last month's sales compare to last year's sales for the same period?
# - What was our total revenue for last month?
# - Which products were the top sellers last month?
# - What revenue was generated from our top-selling product last month?
# - How many units of the TrailMaster X4 Tent were sold last year during the same month?
# - What is the projected sales growth for this month compared to last month?
# - How can we improve sales of our underperforming products?
# - What were the total returns last month?
# - What strategies can we implement to boost sales this quarter?

quantitative_retail_responses = [
    (['total sales last month'], "Last month, our total sales reached $150,000, showing a significant increase compared to previous months."),
    (["last month's sales compare to last year's"], "Last month’s sales increased by 20% compared to the same month last year, where total sales were $125,000. This shows strong growth year-over-year."),
    (["total revenue for last month"], "Our total revenue for last month was $180,000, factoring in both sales and any additional income streams. This represents an increase from $150,000 in revenue during the same period last year."),
    (["top sellers last month"], "The top-selling products last month were:\nCozyNights Sleeping Bag: 1,200 units sold\nTrailMaster X4 Tent: 850 units sold\nTrekReady Hiking Boots: 600 units sold"),
    (["revenue was generated from our top-selling product last month"], "The CozyNights Sleeping Bag generated $60,000 in revenue last month, making it our highest-earning product. Each unit sold for $50."),
    (["units of the trailmaster x4 tent were sold last year during the same month"], "Last year, we sold 600 units of the TrailMaster X4 Tent in the same month, indicating a substantial growth in sales this year with 850 units sold."),
    (["projected sales growth for this month compared to last month"], "With current trends and customer interest, we project a 15% increase in sales for this month, aiming for $172,500 in total sales."),
    (["improve sales of our underperforming products"], "We should analyze customer feedback and sales data for underperforming products such as the TrekStar Hiking Sandals, which sold only 150 units last month. Strategies may include promotional discounts, enhanced marketing efforts, or product bundling."),
    (["total returns last month"], "Last month, we processed $5,000 in returns, which is approximately 3.3% of total sales. Monitoring the reasons for returns will be crucial to reducing this figure in the future."),
    (["strategies can we implement to boost sales this quarter"], "Strategies may include launching limited-time promotions on best-selling products, enhancing online marketing efforts, and introducing new products that align with customer interests as identified through market research.")
]

@app.get("/agent-answers")
def get_agent_answers(domain: str = Query(...), scenario: str = Query(...)):
    # Check for basic AI/general questions
    normalized = scenario.strip().lower()
    for triggers, resp in basic_ai_responses:
        for trig in triggers:
            if trig in normalized:
                # Return same answer for all agents
                if domain == "retail":
                    agent_keys = list(retail_agent_answers.values())[0].keys()
                elif domain == "insurance":
                    agent_keys = list(insurance_agent_answers.values())[0].keys()
                else:
                    agent_keys = []
                return {"answers": {k: resp for k in agent_keys}}
    # Check for quantitative retail questions
    if domain == "retail":
        for triggers, resp in quantitative_retail_responses:
            for trig in triggers:
                if trig in normalized:
                    agent_keys = list(retail_agent_answers.values())[0].keys()
                    return {"answers": {k: resp for k in agent_keys}}

    if domain == "retail":
        answers = retail_agent_answers.get(scenario)
        if answers:
            return {"answers": answers}
        else:
            # Not found: fallback message for all agents
            agent_keys = list(retail_agent_answers.values())[0].keys()
            msg = "I am currently running locally with FastAPI DB. Once I am integrated with AI Foundry, I will be able to answer everything."
            return {"answers": {k: msg for k in agent_keys}}
    elif domain == "insurance":
        norm_scenario = normalize_key(scenario)
        answers = None
        for k, v in insurance_agent_answers.items():
            if normalize_key(k) == norm_scenario:
                answers = v
                break
        if answers:
            return {"answers": answers}
        else:
            agent_keys = list(insurance_agent_answers.values())[0].keys()
            msg = "I am currently running locally with FastAPI DB. Once I am integrated with AI Foundry, I will be able to answer everything."
            return {"answers": {k: msg for k in agent_keys}}
    # Unknown domain: fallback
    return {"answers": {}}