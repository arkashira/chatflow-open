# breakeven.md

## Unit Economics & Break-even Analysis

### Cost per Active User
1. **Compute**: 
   - Estimated cost per user per month: $0.50
   - Assumed usage: 100 active users per server instance
   - Total monthly compute cost per user: $0.50

2. **Storage**: 
   - Estimated cost per user per month: $0.10
   - Average data storage per user: 1 GB
   - Total monthly storage cost per user: $0.10

3. **Bandwidth**: 
   - Estimated cost per user per month: $0.20
   - Average bandwidth usage per user: 5 GB
   - Total monthly bandwidth cost per user: $0.20

**Total Cost per Active User**:  
$$
\text{Total Cost} = \text{Compute} + \text{Storage} + \text{Bandwidth} = 0.50 + 0.10 + 0.20 = \text{USD } 0.80
$$

### Pricing Tiers
1. **Basic Tier**: $15/month
   - Features: Basic chat functionality, 1 agent, 1 GB storage, Email support

2. **Pro Tier**: $30/month
   - Features: Advanced chat features, 5 agents, 5 GB storage, Email + chat support

3. **Enterprise Tier**: $75/month
   - Features: All features, unlimited agents, 20 GB storage, Priority support, Custom integrations

### Customer Acquisition Cost (CAC) Range
- Estimated CAC: $50 - $100 per user
  - Marketing and sales expenses, including advertising, outreach, and promotions.

### Lifetime Value (LTV) Estimate
- Average customer lifespan: 24 months
- Average revenue per user (ARPU) across tiers: $40/month
- LTV Calculation:
$$
\text{LTV} = \text{ARPU} \times \text{Customer Lifespan} = 40 \times 24 = \text{USD } 960
$$

### Break-even Users Count
- Monthly Fixed Costs (Marketing, Development, Support): $2,000
- Contribution Margin per User (Revenue - Cost): 
$$
\text{Contribution Margin} = \text{Price} - \text{Cost} = 40 - 0.80 = \text{USD } 39.20
$$
- Break-even Users Count:
$$
\text{Break-even Users} = \frac{\text{Monthly Fixed Costs}}{\text{Contribution Margin}} = \frac{2000}{39.20} \approx 51 \text{ users}
$$

### Path to $10K MRR
- Target Monthly Recurring Revenue (MRR): $10,000
- Average Revenue per User (ARPU): $40/month
- Required Users:
$$
\text{Required Users} = \frac{\text{Target MRR}}{\text{ARPU}} = \frac{10000}{40} = 250 \text{ users}
$$
- Tier Strategy:
  - If targeting **Pro Tier** ($30/month):
    - Required Users: 
    $$
    \frac{10000}{30} \approx 334 \text{ users}
    $$
  - If targeting **Enterprise Tier** ($75/month):
    - Required Users: 
    $$
    \frac{10000}{75} \approx 134 \text{ users}
    $$

**Summary**: 
- To achieve $10K MRR, we can target 250 users on the Basic Tier, 334 users on the Pro Tier, or 134 users on the Enterprise Tier.