Title: Last Week in Security (LWiS) - 2021-07-12
Date: 2021-07-12 23:59
Category: LWiS
Tags: LWiS, Exploits, Tools
Slug: last-week-in-security-lwis-2021-07-12
Author: Erik
Summary: Arbitrary exe's as BOFs (<a href="https://twitter.com/phraaaaaaa/" target="_blank">@phraaaaaaa</a>), .NET exe's via BOF (<a href="https://twitter.com/anthemtotheego" target="_blank">@anthemtotheego</a>), enterprise grade RCE (<a href="https://twitter.com/AdamOfDc949" target="_blank">@AdamOfDc949</a>), built-in packet sniffing in Windows (<a href="https://twitter.com/TheXC3LL" target="_blank">@TheXC3LL</a>), patching EternalBlue for embedded (<a href="https://twitter.com/CaptMeelo" target="_blank">@CaptMeelo</a>), and more!

<p>Last Week in Security is a summary of the interesting cybersecurity news, techniques, tools and exploits from the previous week. This post covers 2021-07-06 to 2021-07-12.</p>
<section id="news">
<h2>News</h2>
<ul>
<li><a href="https://ag.ny.gov/sites/default/files/utah_v_google.1.complaint_redacted.pdf" target="_blank">Multiple U.S. States Sue Google for Violating Antitrust Laws With Play Store Fees</a>. Last year Google said that all app developers would be required to use the Google Play Store payment system for in-app billing, which comes with a 30% cut to Google. What this means for Apple, who had a trail in May against Epic Games for the same issue (decision pending) remains to be seen.</li>
<li><a href="https://github.com/audacity/audacity/issues/1213" target="_blank">New privacy policy is completely unacceptable!</a>. Audacity was bought by Muse Group (which owns Ultimate Guitar and MuseScore as well) and predictably want telemetry on the user base of their new toy or their lawyers slapped the boilerplate on it to cover all eventualities. Either way, there is now <a href="https://github.com/tenacityteam/tenacity" target="_blank">tenacity</a>.</li>
<li><a href="https://www.bloomberg.com/news/articles/2021-07-06/biden-wants-farmers-to-have-right-to-repair-own-equipment-kqs66nov" target="_blank">Biden Sets Up Tech Showdown With ‘Right-to-Repair’ Rules for FTC</a>. This battle has been brewing for a while as companies push harder against consumers actually owning, well, anything really. With pressure from the top, perhaps a set of FTC rules could give power back to the people and ensure that you do actually own what you buy and are free to modify and repair it on your own.</li>
<li><a href="https://csirt.divd.nl/cases/DIVD-2021-00011/" target="_blank">DIVD-2021-00011 - Kaseya VSA Limited Disclosure</a>. The Dutch CERT found and warned Kaseya about multiple vulnerabilities in April. Was the REvil exploit a case of parallel discovery, or perhaps a compromise of the Kaseya ticketing system?</li>
<li><a href="https://msrc-blog.microsoft.com/2021/07/08/microsoft-bug-bounty-programs-year-in-review-13-6m-in-rewards/" target="_blank">Microsoft Bug Bounty Programs Year in Review: $13.6M in Rewards</a>. While that is a big number, the bug bounty community, and Microsoft specifically have been at the center of some bug bounty drama. Hopefully it encourages more researches to responsibly report vulnerabilities, and other companies to enact their own bug bounty programs.</li>
</ul>
</section>
<section id="techniques">
<h2>Techniques</h2>
<ul>
<li><a href="https://blog.grimm-co.com/2021/07/old-dog-same-tricks.html" target="_blank">Old dog, same tricks</a>. Old "enterprise" software can be a gold mine for bugs. In this post a remote code execution vulnerability in Beagle Software’s ClockWatch is found and exploited. The vendor has declined to update, and thus <a href="https://github.com/grimm-co/NotQuite0DayFriday/tree/trunk/2021.07.07-clockwatch-enterprise" target="_blank">this PoC</a> should work forever (if you ever find ClockWatch in the wild).</li>
<li><a href="https://www.zerodayinitiative.com/blog/2021/7/7/cve-2021-28474-sharepoint-remote-code-execution-via-server-side-control-interpretation-conflict" target="_blank">CVE-2021-28474: SharePoint Remote Code Execution via Server-Side Control Interpretation Conflict</a>. After login, the site creation process leads to deserialization of untrusted user data and the ability to run arbitrary OS commands. This was patched in May 2021.</li>
<li><a href="https://bugs.chromium.org/p/project-zero/issues/detail?id=2189" target="_blank">Issue 2189: mpengine: asprotect embedded runtime dll memory corruption</a>. An old, obscure packer format (asprotect) was emulated by executing an embedded DLL without signature checks. By creating a special asprotect DLL, RCE as SYSTEM on file scan is achievable. How many more obscure format unpackers lie in wait inside defender and similar products?</li>
<li><a href="https://adepts.of0x.cc/pktmon-dissection/" target="_blank">Adding a native sniffer to your implants: decomposing and recomposing PktMon</a>. Following the "write your own tools" mantra, this post explores PktMon and how to write your own packet sniffer using the built in "Packet Monitor" (Win 10/2019 1809+).</li>
<li><a href="https://filesec.io/" target="_blank">Filesec.io</a>. Stay up-to-date with the latest file extensions being used by attackers. It's the LOLBins or GTFObins of file extensions.</li>
<li><a href="https://labs.jumpsec.com/printnightmare-network-analysis/" target="_blank">Printnightmare Network Analysis</a>. This is the kind of analysis that "open source tools" (OSTs) enable. This is a great post on how to break down pcaps to generate network signatures for new techniques/tools.</li>
<li><a href="https://captmeelo.com/pentest/2018/06/26/patching-doublepulsar.html" target="_blank">Patching DoublePulsar to Exploit Windows Embedded Machines</a>. This is a great example of not giving up on the first error, trying harder, and digging into issues to find solutions. Although an Windows Embedded support wasn't added to metasploit, the author got a shell and was able to continue the assessment.</li>
<li><a href="https://iwantmore.pizza/posts/PEzor4.html" target="_blank">Process Creation is Dead, Long Live Process Creation — Adding BOFs Support to PEzor</a>. This is the coolest tool of the last week. Run arbitrary executables as BOFs with a single command in Cobalt Strike. We have reached full BOF weaponization.</li>
</ul>
</section>
<section id="tools-and-exploits">
<h2>Tools and Exploits</h2>
<ul>
<li><a href="https://github.com/rvrsh3ll/TokenTactics" target="_blank">TokenTactics</a> is an Azure JSON Web Token (JWT) manipulation toolset. Based on the work at <a href="https://o365blog.com/aadinternals/" target="_blank">AAD Internals</a>, it adds the ability to pivot between token types, requiring (in certain setups) only one device code phish for wide access into Azure, Teams, Outlook, etc. The target inputs a code into a legitimate Microsoft page, but the codes are only good for 15 minutes.</li>
<li><a href="https://github.com/anthemtotheego/InlineExecute-Assembly" target="_blank">InlineExecute-Assembly</a> is a proof of concept Beacon Object File (BOF) that allows security professionals to perform in process .NET assembly execution as an alternative to Cobalt Strikes traditional fork and run execute-assembly module. InlineExecute-Assembly will execute any assembly with the entry point of Main(string[] args) or Main(). This should allow you to run most released tooling without any prior modification needed. More information in the <a href="https://securityintelligence.com/posts/net-execution-inlineexecute-assembly/" target="_blank">blog post</a>.</li>
<li><a href="https://github.com/immunIT/TeamsUserEnum" target="_blank">TeamsUserEnum</a> will determine if an email is registered on teams or not. More details on <a href="https://www.immunit.ch/blog/2021/07/05/microsoft-teams-user-enumeration/" target="_blank">immunIT's blog</a>.</li>
</ul>
</section>
<section id="new-to-me">
<h2>New to Me</h2>
<p>This section is for news, techniques, and tools that weren't released last week but are new to me. Perhaps you missed them too!</p>
<ul>
<li><a href="https://github.com/ekzhang/rustpad" target="_blank">rustpad</a> is an efficient and minimal collaborative code editor, self-hosted, no database required. Consider this where you would have used Etherpad in the past.</li>
<li><a href="https://github.com/reconmap/reconmap" target="_blank">reconmap</a>. This looks like a great tool to help operators collaborate on an external penetration test or red team engagement.</li>
</ul>
<aside class="m-block m-success">
<h3>Questions or comments?</h3>
<p>Email: blog (at) badsectorlabs.com (<a href="files/pgp_key.txt">PGP Key</a>)</p>
<p>Twitter: <a href="https://twitter.com/badsectorlabs" target="_blank">@badsectorlabs</a></p>
</aside>
<p>Techniques, tools, and exploits linked in this post are not reviewed for quality or safety. Do your own research and testing.
This post is cross-posted on <a href="https://www.sixgen.io/news" target="_blank">SIXGEN's blog</a>.</p>
</section>
