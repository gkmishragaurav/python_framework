# REST API Testing Framework assignment overview:
To solve the problem related to creating a perf test, this document will walk through how different aspects for the same will be
covered.
## Tools/Language used:
Language – Python
Submodules – Unittest for test case simulation, requests for handling REST API layer.
## What is needed in designing an API Testing framework?
1. Engine Layer:
a. There can be multiple Engines in a framework, such as (examples only)
i. Rest engine for handling rest calls.
ii. UI engine for handling UI calls.
iii. XML-RPM layer for RPC calls.
b. These engines will handle any call came for respective type.
c. These engines are non-processing based – means input and output will not be formatted. For serialization and de-
serialization, we will use another layer. This means plain object will be returned.

2. Execute parallel Layer:
a. If above API need to be executed in parallel fashion this layer is needed and important.
3. Library Layer:
a. This layer is to make sure that call is ready to use.
b. We can use this layer for serialization and de-serialization.
c. Respective retry and error handling can be done here.
d. Return should be in a format, which is ready to use for upper layer.
4. Verification Layer:
a. Once any library call is made, some verifications are needed to call it pass.
b. This layer will be collection of all verifications, which can be executed based on demand.
c. Verifications can be divided in type
i. Important – this fail means TC fail
ii. Additional – This fail means TC will not fail
iii. Global – This will run with all kinds of TC

5. Operation Layer:
a. Operation = Library + verification
b. Example, if we are do create_user, it means, user will be related verifications will run. For example, user is present
in DB, user can be seen on UI, user can be listed in API.
c. This will help in creating a scenario.
d. A map of library function to verification can me maintained in a config/json file.
6. Test case Layer:
a. Testcase means arranging different operation in order.
b. It is possible that in a particular case couple of extra verification should be added. That can be done here.
c. If some of the verification should be removed that also can be done here.
d. There can be many ways one can develop and arrange testcases.
i. BDD – development of TC based on business req. Python+gerkin is used for this kind of TCs
ii. TDD – For carry data is files we used TDD ways. You must read the data and accordingly arrange TC.
iii. Custom:
1. Make CSV files for test case itself.
2. Use Unittest from python library to arrange TC. --- I have used this one for this assignment.

7. Test scenario Layer:
a. A test scenario means a mix of few Testcases. Can be one testcase as well.
8. Logging and reporting layer:
a. Logging is important to troubleshooting at later stage.
b. Use logging module from python.
i. Log rotation should be handled. As in preserve the log for previous run, if new run to be taken.
ii. Arrange different level of logging – INFO, DEBUG, ERROR.
c. Once everything is done we need to create a report which can walk us through all Operation that we have executed,
All verifications should be attached to that operation, and if there is any data in support of these verifications, that
should also be dumped here. An HTML report will support all of it.
