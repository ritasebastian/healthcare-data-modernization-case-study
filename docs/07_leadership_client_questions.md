# 7. Leadership & Client-Facing Questions

## Director mindset

Do not answer every question with “I would code it.”

Show how you scale yourself through:

- architecture standards
- reusable templates
- code review
- design review
- mentoring
- risk management
- documentation
- decision records
- release gates

## Q: Four hospital engagements are running at once. How do you maintain quality?

Strong answer:

> “I would standardize what should be standard—landing zone, security baseline, Terraform modules, CI/CD, ingestion framework, observability and review gates—while allowing source-specific design where necessary. Each engagement gets architecture review, security review, code review, data-quality validation and production-readiness checks. I would personally focus on the highest-risk decisions and unblock the team rather than becoming the bottleneck for every implementation detail.”

## Q: Engineer disagrees with your architecture

Use:

**Goal → constraints → options → evidence → decision → document**

> “I would ask them to frame the alternative in terms of requirements, risks, complexity, cost and delivery timeline. If their option is better, I would change the design. The goal is the best engineering decision, not defending my original idea.”

## Q: Client asks for an unrealistic six-week migration

> “I would separate must-have outcomes from ideal-state outcomes, identify critical path dependencies, and propose a phased plan. I would be explicit about risks rather than quietly accepting impossible scope. A realistic first phase may be the secure landing zone plus two priority sources and validated handoff, with remaining sources sequenced afterward.”

## Q: CIO asks why modernization matters

Avoid jargon.

Say:

> “Today every new integration requires custom work and manual handling. The new platform creates repeatable ingestion, governance and sharing patterns, which reduces onboarding time, lowers operational risk, and gives analytics and AI teams access to trusted data faster.”

## Q: When do you personally get hands-on?

> “I stay close to architecture, code reviews and difficult technical decisions, and I will pair with engineers or build critical components when risk is high. But I also need to make the team stronger, so I avoid owning every line of code myself.”

## Q: What makes a good handoff?

> “The receiving team can deploy, monitor, troubleshoot, recover and modify the platform without depending on the original project team.”
