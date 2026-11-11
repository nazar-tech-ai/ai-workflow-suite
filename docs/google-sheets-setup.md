# Google Sheets setup

Create one spreadsheet with a tab per workflow below; the header row must contain the listed columns (exact names). In each Google Sheets node, select your spreadsheet and tab — the repo ships `YOUR_GOOGLE_SHEET_ID` as a placeholder and the tab names below are only suggestions (taken from the original export).

## `03-workflow-cost-estimator.json`
Node `Append row in sheet` · operation `append` · suggested tab **Sheet1**

`Requirement`, `Workflow Name`, `Project Rating`, `Business Value`, `Difficulty`, `Estimated Hours`, `Automation Level`, `Freelancer Price`, `Agency Price`, `Timeline`, `Developer Level`, `ROI`, `Reason`, `Created At`, `Search Score`

## `04-proposal-generator.json`
Node `Google Sheets` · operation `append` · suggested tab **Sheet2**

`Requirement`, `Workflow Name`, `Search Score`, `Scope of Work`, `Project Summary`, `Proposal Title`, `Deliverables`, `Timeline`, `Pricing`, `Technologies`, `Assumptions`, `Next Steps`, `Created At`, `Project Rating`, `Business Value`, `Difficulty`, `Estimated Hours`, `Automation Level`

## `05-workflow-generator.json`
Node `Google Sheets1` · operation `append` · suggested tab **Sheet3**

`Requirement`, `Workflow Name`, `Search Score`, `Project Rating`, `Business Value`, `Difficulty`, `Estimated Hours`, `Automation Level`, `Workflow Title`, `Business Overview`, `Trigger Node`, `Required Nodes`, `Workflow Logic`, `Implementation Steps`, `Integrations`, `Error Handling`, `Complexity`, `Future Enhancements`, `Created At`

## `06-workflow-consultant.json`
Node `Google Sheets1` · operation `append` · suggested tab **Project 6**

`Requirement`, `Workflow Name`, `Search Score`, `Project Rating`, `Business Value`, `Difficulty`, `Estimated Hours`, `Automation Level`, `Consultation Title`, `Business Analysis`, `Recommended Solution`, `Recommended Workflow`, `Implementation Strategy`, `Estimated ROI`, `Risk Level`, `Business Impact`, `Recommendation`, `Next Steps`, `Created At`

## `07-workflow-optimizer.json`
Node `Google Sheets1` · operation `append` · suggested tab **Project 7**

`Requirement`, `Workflow Name`, `Search Score`, `Project Rating`, `Business Value`, `Difficulty`, `Estimated Hours`, `Automation Level`, `Optimization Title`, `Current Analysis`, `Performance Improvements`, `Cost Optimization`, `Node Optimization`, `Scalability Recommendations`, `Security Recommendations`, `Best Practices`, `Estimated Performance Gain`, `Final Recommendation`, `Created At`

## `08-workflow-validator.json`
Node `Google Sheets1` · operation `append` · suggested tab **Project 8**

`Requirement`, `Workflow Name`, `Search Score`, `Project Rating`, `Business Value`, `Difficulty`, `Estimated Hours`, `Automation Level`, `Validation Title`, `Overall Status`, `Workflow Completeness`, `Logic Validation`, `Node Validation`, `Integration Validation`, `Security Validation`, `Performance Validation`, `Issues Found`, `Recommendation`, `Created At`

## `09-documentation-generator.json`
Node `Google Sheets1` · operation `append` · suggested tab **Project 9**

`Requirement`, `Workflow Name`, `Search Score`, `Project Rating`, `Business Value`, `Difficulty`, `Estimated Hours`, `Automation Level`, `Documentation Title`, `Executive Summary`, `Business Overview`, `Workflow Architecture`, `Required Nodes`, `Implementation Steps`, `Workflow Logic`, `Integrations`, `Error Handling`, `Best Practices`, `Deployment Guide`, `Future Enhancements`, `HTML Document`, `Created At`

## `10-deployment-assistant.json`
Node `Google Sheets1` · operation `append` · suggested tab **Project 10**

`Requirement`, `Workflow Name`, `Search Score`, `Project Rating`, `Business Value`, `Difficulty`, `Estimated Hours`, `Automation Level`, `Deployment Title`, `Deployment Strategy`, `Required Services`, `Environment Setup`, `Deployment Steps`, `Security Configuration`, `Monitoring Strategy`, `Backup Strategy`, `Maintenance Plan`, `Deployment Checklist`, `Created At`

## `11-recommendation-engine.json`
Node `Google Sheets1` · operation `append` · suggested tab **Project 11**

`Requirement`, `Recommended Workflow`, `Recommendation Title`, `Business Requirement Analysis`, `Recommendation Reason`, `Alternative Workflows`, `Comparison Summary`, `Business Benefits`, `Estimated ROI`, `Implementation Priority`, `Confidence Score`, `Final Recommendation`, `Best Search Score`, `Search Status`, `Created At`, `Total Matches`

## `13-monitoring-analytics.json`
Node `Google Sheets1` · operation `append` · suggested tab **Project 13**

`workflow_name`, `workflow_category`, `performance_score`, `automation_score`, `complexity`, `scalability`, `maintainability`, `cost_efficiency`, `business_impact`, `strengths`, `weaknesses`, `improvement_suggestions`

## `21-linkedin-profile-enrichment.json`
Node `Get profiles to enrich` · operation `append` · suggested tab **Sheet1**



## `21-linkedin-profile-enrichment.json`
Node `Update row in sheet` · operation `update` · suggested tab **Sheet1** · matches rows on `LinkedIn URL`

`LinkedIn URL`, `First name`, `Last name`, `Headline`, `Job title`, `Company name`, `Country`, `City`, `Summary`, `Skills`, `Positions`, `Educations`, `Certifications`, `created`, `trackingId`, `firstName`, `lastName`, `pronoun`, `versionTag`, `headline`, `publicIdentifier`, `creator`, `influencer`, `premium`, `connectionType`, `birthDate`, `profileId`, `pictureUrl`, `coverImageUrl`, `countryCode`, `geoUrn`, `geoLocationName`, `geoCountryName`, `jobTitle`, `positions`, `educations`, `certifications`, `courses`, `honors`, `languages`, `volunteerExperiences`, `projects`, `publications`, `patents`, `testScores`, `organizations`, `volunteerCauses`, `companyName`, `companyPublicId`, `companyLinkedinUrl`, `currentCompany`, `followerCount`, `mutualConnections`, `isVerified`, `verificationBadge`, `availablePremiumFeatures`, `pronunciationUrl`, `connectionsCount`, `skills`, `inputUrl`, `id`
