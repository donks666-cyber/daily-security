Title: Last Week in Security (LWiS) - 2022-06-06
Date: 2022-06-06 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2022-06-06
Author: Erik
Summary: Confluence RCE, Open Redirect -&gt; RCE (<a href="https://twitter.com/ByQwert" target="_blank">@ByQwert</a>), U-Boot vulns (<a href="https://twitter.com/NCCGroupInfosec" target="_blank">@NCCGroupInfosec</a>), Azure Managed Identity attacks (<a href="https://twitter.com/_wald0" target="_blank">@_wald0</a>), Deep Learning password extraction (<a href="https://twitter.com/HarmJ0y" target="_blank">@harmj0y</a>), LSASS cryptography (<a href="https://twitter.com/skelsec" target="_blank">@SkelSec</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the past week. This post covers 2022-05-30 to 2022-06-06.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://cloud.google.com/blog/products/identity-security/announcing-psp-security-protocol-is-now-open-source" target="_blank">Announcing PSP's cryptographic hardware offload at scale is now open source</a>. What happens when the NSA draws a <a href="https://www.businessinsider.com/leaked-nsa-slide-of-google-cloud-2013-10" target="_blank">smiley face</a> on your network map? You spend a decade perfecting encryption that you can offload to smart NICs so that all traffic is encrypted in transit. I wonder where the next smiley face will be drawn...</li>
<li><a href="https://confluence.atlassian.com/doc/confluence-security-advisory-2022-06-02-1130377146.html" target="_blank">Confluence Server and Data Center - CVE-2022-26134 - Critical severity unauthenticated remote code execution vulnerability</a>. "Atlassian has been made aware of current active exploitation of a critical severity unauthenticated remote code execution vulnerability in Confluence Data Center and Server. The OGNL injection vulnerability allows an unauthenticated user to execute arbitrary code on a Confluence Server or Data Center instance."</li>
<li><a href="https://www.federalregister.gov/documents/2022/05/26/2022-11282/information-security-controls-cybersecurity-items" target="_blank">Information Security Controls: Cybersecurity Items</a>. The US joins Europe with its own "Wassenaar Arrangement" rule by the Industry and Security Bureau. TLDR don't sell cyber capabilities to <a href="https://www.law.cornell.edu/cfr/text/15/appendix-Supplement_No_1_to_part_740" target="_blank">Country Group D</a>.</li>
</ul>
</section>
<section id="techniques-and-write-ups">
<h2>Techniques and Write-ups</h2>
<ul>
<li><a href="https://macrosec.tech/index.php/2022/06/01/abusing-cve-2022-26923-through-socks5-on-a-mythic-c2-agent/" target="_blank">Abusing CVE-2022-26923 Through SOCKS5 on a Mythic C2 Agent</a>. This post explores the AD CS vulnerability but uses Mythic an an Apollo agent with SOCKS forwarding to pull it off. Nice practical usage example!</li>
<li><a href="https://medium.com/@byq/from-open-redirect-to-rce-in-one-week-66a7f73fd082" target="_blank">From open redirect to RCE in one week</a>. This is a wild ride through a series of strange small bugs that result in full RCE. Web app hackers take note.</li>
<li><a href="https://research.nccgroup.com/2022/06/03/technical-advisory-multiple-vulnerabilities-in-u-boot-cve-2022-30790-cve-2022-30552/" target="_blank">Technical Advisory - Multiple Vulnerabilities in U-Boot (CVE-2022-30790, CVE-2022-30552)</a>. This one is for the embedded device hackers (and chromebook hackers).</li>
<li><a href="https://posts.specterops.io/managed-identity-attack-paths-part-1-automation-accounts-82667d17187a" target="_blank">Managed Identity Attack Paths, Part 1: Automation Accounts</a>. Azure Automation Accounts, Logic Apps, and Function Apps all use "Managed Identity assignments" which allows scripts to authenticate as a specific Service Principle. These services can be used by an attacker to leak their JWT which can be used to authenticate outside the context of the Authentication Account.</li>
<li><a href="https://posts.specterops.io/deeppass-finding-passwords-with-deep-learning-4d31c534cd00" target="_blank">DeepPass — Finding Passwords With Deep Learning</a>. It's starting to feel like Will is lining up a career change into data science, but as long as he keeps the red team angle I'm here for it. Here he trains a model (<a href="https://github.com/GhostPack/DeepPass" target="_blank">DeepPass</a>) to recognize passwords in arbitrary documents. How long before this is repackaged and sold as "AI/ML deep learning information disclosure hunter 9000" at RSA?</li>
<li><a href="https://skelsec.medium.com/lsass-needs-an-iv-57b7333d50d8" target="_blank">LSASS needs an IV</a>. Spoiler: It doesn't really need an IV if you can guess a few characters of a password. Interesting deep dive into the (poor?) cryptographic decisions in LSASS.</li>
<li><a href="https://infosecwriteups.com/enumeration-and-lateral-movement-in-gcp-environments-c3b82d342794" target="_blank">Enumeration and lateral movement in GCP environments</a>. Lateral movement is more fun in the cloud.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/nickvourd/COM-Hunter" target="_blank">COM-Hunter</a> - COM Hijacking voodoo.</li>
<li><a href="https://bitbucket.org/Pirates-of-Silicon-Hills/voightkampff/src/master/" target="_blank">VoightKampff</a> - Beating Google ReCaptcha and the funCaptcha using AWS Rekognition.</li>
<li><a href="https://github.com/Idov31/Nidhogg" target="_blank">Nidhogg</a> Nidhogg is an all-in-one simple to use rootkit for red teams.</li>
</ul>
</section>
<section id="new-to-me-and-miscellaneous">
<h2>New to Me and Miscellaneous</h2>
<p>This section is for news, techniques, write-ups, tools, and off-topic items that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://www.newyorker.com/magazine/2022/06/13/the-surreal-case-of-a-cia-hackers-revenge" target="_blank">The Surreal Case of a C.I.A. Hacker's Revenge</a>. I haven't read this one yet but its on my list.</li>
</ul>
<aside class="m-frame">
<h3>Stats</h3>
<p>Twitter accounts monitored: 416 (+0)</p>
<p>Blogs monitored: 310 (+2)</p>
</aside>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
