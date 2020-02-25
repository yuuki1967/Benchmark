# OWASP Benchmark
The OWASP Benchmark Project is a Java test suite designed to verify the speed and accuracy of vulnerability detection tools. It is a fully runnable open source web application that can be analyzed by any type of Application Security Testing (AST) tool, including SAST, DAST (like <a href="https://www.owasp.org/index.php/ZAP">OWASP ZAP</a>), and IAST tools. The intent is that all the vulnerabilities deliberately included in and scored by the Benchmark are actually exploitable so its a fair test for any kind of application vulnerability detection tool. The Benchmark also includes scorecard generators for numerous open source and commercial AST tools, and the set of supported tools is growing all the time. 

The project documentation is all on the OWASP site at the <a href="https://www.owasp.org/index.php/Benchmark">OWASP Benchmark</a> project pages. Please refer to that site for all the project details.

The current latest release is v1.2. Note that all the releases that are available here: https://github.com/OWASP/Benchmark/releases, are historical. The latest release is always available live by simply cloning or pulling the head of this repository (i.e., git pull).

# Benchmark
Please read HOW_TO_USE for getting the scorecard of analyzed result by CxIAST.

![cxIAST_snapshot](https://github.com/yuuki1967/Benchmark/blob/master/scorecard/CxIAST_snapshot.png)

# Benchmark Result with CxIAST 3.4.0

![scorecard](https://github.com/yuuki1967/Benchmark/blob/master/scorecard/Benchmark_v1.2_Scorecard_for_CxIAST.png)
