#!/usr/bin/env python3
import base64
import os
from pathlib import Path

# Base path
BASE_PATH = Path("/Users/admin/Downloads/포트폴리오/website")

# Read CSS
with open(BASE_PATH / "css/style.css", "r") as f:
    css_content = f.read()

# Function to encode image to base64
def img_to_base64(img_path):
    try:
        with open(img_path, "rb") as f:
            data = base64.b64encode(f.read()).decode()
            ext = img_path.suffix.lower()
            mime = "image/png" if ext == ".png" else "image/jpeg"
            return f"data:{mime};base64,{data}"
    except:
        return ""

# Encode ADBIAS images
adbias_images = {
    "figure_mean_qwk": img_to_base64(BASE_PATH / "assets/adbias/figure_mean_qwk.png"),
    "figure_mean_severity": img_to_base64(BASE_PATH / "assets/adbias/figure_mean_severity.png"),
    "adbias_pipeline": img_to_base64(BASE_PATH / "assets/adbias/adbias_pipeline.png"),
    "figure_MFRM": img_to_base64(BASE_PATH / "assets/adbias/figure_MFRM.png"),
}

# PDF-specific CSS additions
pdf_css = """
@page {
    size: A4;
    margin: 2cm 1.5cm;
}
body {
    font-size: 11pt;
}
.nav, .cta-section, .cta-buttons, .back-link, .project-link {
    display: none !important;
}
.hero {
    padding: 20px 0 40px;
}
.hero h1 {
    font-size: 36pt;
}
.section, .project-content-section {
    padding: 30px 0;
    page-break-inside: avoid;
}
.project-section {
    page-break-before: always;
}
.project-section:first-of-type {
    page-break-before: auto;
}
h1, h2, h3 {
    page-break-after: avoid;
}
.code-block {
    font-size: 9pt;
    page-break-inside: avoid;
}
.code-block pre {
    white-space: pre-wrap;
    word-wrap: break-word;
}
table {
    font-size: 10pt;
    page-break-inside: avoid;
}
.image-block {
    page-break-inside: avoid;
}
.image-block img {
    max-height: 300px;
    object-fit: contain;
}
.skills-grid {
    grid-template-columns: repeat(2, 1fr);
}
.project-card {
    page-break-inside: avoid;
}
.arch-item {
    page-break-inside: avoid;
}
.contact-grid {
    grid-template-columns: repeat(3, 1fr);
}
.pdf-section-title {
    font-size: 28pt;
    font-weight: 700;
    color: #2563eb;
    margin: 40px 0 20px;
    padding-bottom: 10px;
    border-bottom: 2px solid #2563eb;
}
"""

html_content = f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>Yunho Jang - AI Engineer Portfolio</title>
    <style>
{css_content}
{pdf_css}
    </style>
</head>
<body>
    <!-- Hero -->
    <section class="hero" style="padding-top: 20px;">
        <div class="container">
            <span class="hero-label">AI Engineer</span>
            <h1>장윤호 (Yunho Jang)</h1>
            <p class="hero-subtitle">
                Multi-LLM 시스템, 자연어 처리, 딥러닝 연구에 집중하는 AI 엔지니어입니다.
            </p>
            <div style="display: flex; gap: 24px; font-size: 14px; color: #6b7280;">
                <span>GitHub: github.com/joyuno</span>
                <span>Email: joy981017@gmail.com</span>
            </div>
        </div>
    </section>

    <!-- About -->
    <section class="section">
        <div class="container">
            <div class="section-title">About</div>
            <div class="about-content">
                <div class="about-text">
                    <p>
                        Large Language Model(LLM)의 편향 분석 및 Multi-Agent 시스템 연구를 진행하고 있습니다.
                        교육 분야에서의 AI 적용에 관심을 가지고, 특히 자동 에세이 채점 시스템의 공정성과 신뢰성 향상을
                        목표로 연구하고 있습니다.
                    </p>
                    <p>
                        ACL 2025에 ADBIAS 프레임워크를 제출하여 Multi-LLM 협업 및 편향 조정 방법론을 제안했으며,
                        LG U+ 인턴십에서는 웹 크롤링 및 감성 분석 기반 업무 자동화 시스템을 구축했습니다.
                    </p>
                </div>
                <div class="about-info">
                    <div class="info-item">
                        <span class="info-label">Focus</span>
                        <span class="info-value">NLP, LLM, Data Engineering</span>
                    </div>
                    <div class="info-item">
                        <span class="info-label">Experience</span>
                        <span class="info-value">LG U+ Intern (2025)</span>
                    </div>
                    <div class="info-item">
                        <span class="info-label">Location</span>
                        <span class="info-value">Seoul, Korea</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Skills -->
    <section class="section">
        <div class="container">
            <div class="section-title">Skills</div>
            <div class="skills-grid">
                <div class="skill-category">
                    <h3>AI / ML</h3>
                    <div class="skill-list">
                        <span class="skill-tag">PyTorch</span>
                        <span class="skill-tag">TensorFlow</span>
                        <span class="skill-tag">Transformers</span>
                        <span class="skill-tag">LangChain</span>
                        <span class="skill-tag">scikit-learn</span>
                    </div>
                </div>
                <div class="skill-category">
                    <h3>LLM APIs</h3>
                    <div class="skill-list">
                        <span class="skill-tag">OpenAI API</span>
                        <span class="skill-tag">Anthropic API</span>
                        <span class="skill-tag">Google AI</span>
                        <span class="skill-tag">LLaMA</span>
                    </div>
                </div>
                <div class="skill-category">
                    <h3>Backend</h3>
                    <div class="skill-list">
                        <span class="skill-tag">Python</span>
                        <span class="skill-tag">FastAPI</span>
                        <span class="skill-tag">Node.js</span>
                        <span class="skill-tag">Next.js</span>
                    </div>
                </div>
                <div class="skill-category">
                    <h3>Data & Tools</h3>
                    <div class="skill-list">
                        <span class="skill-tag">PostgreSQL</span>
                        <span class="skill-tag">Supabase</span>
                        <span class="skill-tag">Docker</span>
                        <span class="skill-tag">GitHub Actions</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Projects Overview -->
    <section class="section">
        <div class="container">
            <div class="section-title">Projects</div>
            <div class="projects-list">
                <div class="project-card">
                    <div class="project-meta">
                        <span class="project-type">AI Research</span>
                        <h3>ADBIAS</h3>
                        <span class="project-period">2025</span>
                    </div>
                    <div class="project-content">
                        <p>Multi-LLM 편향 조정 자동 에세이 채점 프레임워크. ACL 2025 제출.</p>
                        <div class="project-tech">
                            <span class="tech-badge">PyTorch</span>
                            <span class="tech-badge">OpenAI API</span>
                            <span class="tech-badge">MFRM</span>
                        </div>
                    </div>
                </div>
                <div class="project-card">
                    <div class="project-meta">
                        <span class="project-type">AI Product</span>
                        <h3>AIIV - AI Mock Interview</h3>
                        <span class="project-period">2025</span>
                    </div>
                    <div class="project-content">
                        <p>실시간 음성 AI 모의면접 서비스. aiiv.site 배포 운영 중.</p>
                        <div class="project-tech">
                            <span class="tech-badge">Next.js</span>
                            <span class="tech-badge">OpenAI</span>
                            <span class="tech-badge">RAG</span>
                        </div>
                    </div>
                </div>
                <div class="project-card">
                    <div class="project-meta">
                        <span class="project-type">AI / Voice Cloning</span>
                        <h3>Talet - AI Voice Fairy Tale</h3>
                        <span class="project-period">2025</span>
                    </div>
                    <div class="project-content">
                        <p>다문화 가정을 위한 AI 음성 전래동화 서비스. XTTS v2 파인튜닝.</p>
                        <div class="project-tech">
                            <span class="tech-badge">PyTorch</span>
                            <span class="tech-badge">XTTS v2</span>
                            <span class="tech-badge">FastAPI</span>
                        </div>
                    </div>
                </div>
                <div class="project-card">
                    <div class="project-meta">
                        <span class="project-type">Data Engineering</span>
                        <h3>LG U+ MVNO Automation</h3>
                        <span class="project-period">2025</span>
                    </div>
                    <div class="project-content">
                        <p>경쟁사 요금제 크롤링, 감성 분석, 자동 리포트 시스템.</p>
                        <div class="project-tech">
                            <span class="tech-badge">Python</span>
                            <span class="tech-badge">Selenium</span>
                            <span class="tech-badge">GitHub Actions</span>
                        </div>
                    </div>
                </div>
                <div class="project-card">
                    <div class="project-meta">
                        <span class="project-type">Web Development</span>
                        <h3>MovieMania</h3>
                        <span class="project-period">2021</span>
                    </div>
                    <div class="project-content">
                        <p>Spring Boot 기반 영화 커뮤니티 웹 애플리케이션.</p>
                        <div class="project-tech">
                            <span class="tech-badge">Java</span>
                            <span class="tech-badge">Spring Boot</span>
                            <span class="tech-badge">MyBatis</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- ADBIAS Detail -->
    <div class="project-section">
        <section class="project-content-section">
            <div class="container">
                <h2 class="pdf-section-title">ADBIAS - Multi-LLM Bias Adjustment</h2>
                <p>
                    <strong>ADBIAS (Adjusting Multi-LLM Biases)</strong>는 자동 에세이 채점(AES) 시스템에서
                    여러 LLM의 채점 편향을 정량적으로 측정하고 보정하여 더 공정하고 신뢰성 있는
                    평가를 가능하게 하는 Multi-Agent 프레임워크입니다.
                </p>

                <h3>Key Results</h3>
                <div class="table-wrap">
                    <table>
                        <thead>
                            <tr><th>Metric</th><th>Baseline</th><th>ADBIAS</th><th>Improvement</th></tr>
                        </thead>
                        <tbody>
                            <tr class="highlight"><td>Accuracy (QWK)</td><td>0.4326</td><td>0.4600</td><td><strong>+6.4%</strong></td></tr>
                            <tr class="highlight"><td>Bias Variance</td><td>0.00192</td><td>0.00081</td><td><strong>-57.9%</strong></td></tr>
                        </tbody>
                    </table>
                </div>

                <div class="image-grid">
                    <div class="image-block">
                        <img src="{adbias_images['figure_mean_qwk']}" alt="Mean QWK">
                        <div class="image-caption">Mean QWK: Meta-LLM vs Individual LLMs</div>
                    </div>
                    <div class="image-block">
                        <img src="{adbias_images['figure_mean_severity']}" alt="Mean Severity">
                        <div class="image-caption">Mean Severity: Bias Reduction Effect</div>
                    </div>
                </div>

                <h3>System Architecture</h3>
                <div class="image-block">
                    <img src="{adbias_images['adbias_pipeline']}" alt="ADBIAS Pipeline">
                    <div class="image-caption">ADBIAS 3-Stage Pipeline Architecture</div>
                </div>

                <div class="architecture-list">
                    <div class="arch-item">
                        <div class="arch-number">1</div>
                        <div class="arch-content">
                            <h4>Multi-LLM Independent Evaluation</h4>
                            <p>4개의 LLM(GPT-4o, Claude 3.5, Gemini 2.5, LLaMA 4)이 동일한 에세이를 독립적으로 평가.</p>
                        </div>
                    </div>
                    <div class="arch-item">
                        <div class="arch-number">2</div>
                        <div class="arch-content">
                            <h4>MFRM-based Bias Quantification</h4>
                            <p>Many-Facet Rasch Model을 적용하여 각 모델의 채점 엄격도(β)를 통계적으로 측정.</p>
                        </div>
                    </div>
                    <div class="arch-item">
                        <div class="arch-number">3</div>
                        <div class="arch-content">
                            <h4>Meta-LLM Bias-Aware Aggregation</h4>
                            <p>Meta-LLM이 원본 에세이, Peer 점수/근거, 편향 메타데이터를 종합하여 최종 점수 생성.</p>
                        </div>
                    </div>
                </div>

                <h3>MFRM Model</h3>
                <div class="image-block">
                    <img src="{adbias_images['figure_MFRM']}" alt="MFRM Model">
                    <div class="image-caption">MFRM Parameter Estimation</div>
                </div>
            </div>
        </section>
    </div>

    <!-- AIIV Detail -->
    <div class="project-section">
        <section class="project-content-section">
            <div class="container">
                <h2 class="pdf-section-title">AIIV - AI Mock Interview</h2>
                <p>
                    <strong>AIIV</strong>는 AI 면접관과 실시간 음성 대화를 통해 면접을 연습할 수 있는 서비스입니다.
                    RAG 파이프라인으로 이력서/자소서를 분석하여 맞춤형 질문을 생성하고,
                    음성 분석을 통해 말하기 패턴 피드백을 제공합니다. aiiv.site에서 서비스 운영 중.
                </p>

                <div class="info-box">
                    <h4>Key Metrics</h4>
                    <p>
                        <strong>End-to-End Latency</strong>: 1.6~2.5초 (음성 입력 → AI 응답 재생 시작)<br>
                        <strong>RAG Precision</strong>: Hybrid Search + Reranking으로 40-60% 정확도 향상
                    </p>
                </div>

                <h3>Core Features</h3>
                <div class="architecture-list">
                    <div class="arch-item">
                        <div class="arch-number">1</div>
                        <div class="arch-content">
                            <h4>Real-time Voice Interview</h4>
                            <p>SSE 기반 스트리밍: Whisper STT → GPT-4o → OpenAI TTS</p>
                        </div>
                    </div>
                    <div class="arch-item">
                        <div class="arch-number">2</div>
                        <div class="arch-content">
                            <h4>Document RAG Pipeline</h4>
                            <p>한국어 자소서 분석, LlamaParse PDF 처리, Hybrid Search (Vector + BM25)</p>
                        </div>
                    </div>
                    <div class="arch-item">
                        <div class="arch-number">3</div>
                        <div class="arch-content">
                            <h4>Voice Pattern Analysis</h4>
                            <p>WPM 계산, 습관어 탐지, 자신감 점수화 및 피드백</p>
                        </div>
                    </div>
                </div>

                <h3>Tech Stack</h3>
                <div class="skills-grid">
                    <div class="skill-category">
                        <h3>Frontend</h3>
                        <div class="skill-list">
                            <span class="skill-tag">Next.js</span>
                            <span class="skill-tag">TypeScript</span>
                            <span class="skill-tag">Tailwind CSS</span>
                        </div>
                    </div>
                    <div class="skill-category">
                        <h3>Backend / AI</h3>
                        <div class="skill-list">
                            <span class="skill-tag">OpenAI GPT-4o</span>
                            <span class="skill-tag">Whisper STT</span>
                            <span class="skill-tag">Cohere Rerank</span>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </div>

    <!-- Talet Detail -->
    <div class="project-section">
        <section class="project-content-section">
            <div class="container">
                <h2 class="pdf-section-title">Talet - AI Voice Fairy Tale</h2>
                <p>
                    다문화 가정을 위한 AI 음성 전래동화 서비스입니다.
                    AIHub의 외국인 한국어 발화 데이터셋을 활용하여 XTTS v2 TTS 모델을 파인튜닝하고,
                    부모님 목소리로 한국어 전래동화를 낭독하는 보이스 클로닝 시스템을 구축했습니다.
                </p>

                <div class="info-box">
                    <h4>담당 업무 (AI/ML Lead)</h4>
                    <p>
                        <strong>데이터</strong>: AIHub 외국인 한국어 발화 데이터 전처리<br>
                        <strong>모델</strong>: XTTS v2 다국어(중국어, 영어, 일본어, 태국어, 베트남어) 파인튜닝<br>
                        <strong>서비스</strong>: FastAPI 기반 TTS REST API 서버 개발
                    </p>
                </div>

                <h3>Technical Implementation</h3>
                <div class="architecture-list">
                    <div class="arch-item">
                        <div class="arch-number">1</div>
                        <div class="arch-content">
                            <h4>Multi-accent Korean TTS</h4>
                            <p>5개국 억양의 한국어 음성 합성 모델 구축</p>
                        </div>
                    </div>
                    <div class="arch-item">
                        <div class="arch-number">2</div>
                        <div class="arch-content">
                            <h4>Zero-shot Voice Cloning</h4>
                            <p>3-10초 음성 샘플만으로 사용자 목소리 복제</p>
                        </div>
                    </div>
                    <div class="arch-item">
                        <div class="arch-number">3</div>
                        <div class="arch-content">
                            <h4>Streaming Architecture</h4>
                            <p>AsyncGenerator 기반 실시간 스트리밍</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </div>

    <!-- LG U+ Detail -->
    <div class="project-section">
        <section class="project-content-section">
            <div class="container">
                <h2 class="pdf-section-title">LG U+ MVNO Automation</h2>
                <p>
                    LG U+ MVNO 사업팀에서 사무 인턴으로 근무하며 <strong>경쟁사 요금제 모니터링</strong>,
                    <strong>뉴스 감성 분석</strong>, <strong>커뮤니티 여론 분석</strong> 업무를 자동화했습니다.
                </p>

                <h3>Key Deliverables</h3>
                <div class="architecture-list">
                    <div class="arch-item">
                        <div class="arch-number">1</div>
                        <div class="arch-content">
                            <h4>MVNO Promotion Crawler</h4>
                            <p>7개 경쟁사 사이트에서 요금제 정보를 자동 수집하고 비교 분석 리포트 생성</p>
                        </div>
                    </div>
                    <div class="arch-item">
                        <div class="arch-number">2</div>
                        <div class="arch-content">
                            <h4>Daily Automated Report System</h4>
                            <p>GitHub Actions로 매일 오전 7:30 자동 실행, Excel 리포트 이메일 발송</p>
                        </div>
                    </div>
                    <div class="arch-item">
                        <div class="arch-number">3</div>
                        <div class="arch-content">
                            <h4>News & Community Sentiment Analysis</h4>
                            <p>Naver API + HuggingFace 감성 분석 모델로 긍정 뉴스 자동 추출</p>
                        </div>
                    </div>
                </div>

                <h3>Results & Impact</h3>
                <ul>
                    <li><strong>업무 자동화</strong>: 매일 2-3시간 소요되던 수동 조사 업무를 완전 자동화</li>
                    <li><strong>데이터 정확성</strong>: 수동 입력 오류 제거, 일관된 데이터 포맷 유지</li>
                    <li><strong>실시간 모니터링</strong>: 경쟁사 가격 변동 및 프로모션 즉시 감지</li>
                </ul>
            </div>
        </section>
    </div>

    <!-- MovieMania Detail -->
    <div class="project-section">
        <section class="project-content-section">
            <div class="container">
                <h2 class="pdf-section-title">MovieMania</h2>
                <p>
                    <strong>MovieMania</strong>는 Spring Boot 기반 영화 커뮤니티 웹 애플리케이션입니다.
                    자유게시판, 영화 리뷰 게시판, 시사회 신청/추첨 기능을 구현한 풀스택 프로젝트입니다.
                </p>

                <h3>Key Features</h3>
                <div class="architecture-list">
                    <div class="arch-item">
                        <div class="arch-number">1</div>
                        <div class="arch-content">
                            <h4>Multi-Board System</h4>
                            <p>자유게시판, 영화 리뷰 게시판, 공지사항 게시판. 페이지네이션, 검색 기능 포함.</p>
                        </div>
                    </div>
                    <div class="arch-item">
                        <div class="arch-number">2</div>
                        <div class="arch-content">
                            <h4>Premiere Application System</h4>
                            <p>시사회 정보 등록 및 사용자 응모, 관리자 추첨 시스템.</p>
                        </div>
                    </div>
                    <div class="arch-item">
                        <div class="arch-number">3</div>
                        <div class="arch-content">
                            <h4>User Authentication</h4>
                            <p>Spring Security 기반 로그인/회원가입, ROLE 기반 권한 관리.</p>
                        </div>
                    </div>
                </div>

                <h3>Tech Stack</h3>
                <div class="skills-grid">
                    <div class="skill-category">
                        <h3>Backend</h3>
                        <div class="skill-list">
                            <span class="skill-tag">Java 11</span>
                            <span class="skill-tag">Spring Boot</span>
                            <span class="skill-tag">Spring Security</span>
                            <span class="skill-tag">MyBatis</span>
                        </div>
                    </div>
                    <div class="skill-category">
                        <h3>Frontend</h3>
                        <div class="skill-list">
                            <span class="skill-tag">JSP</span>
                            <span class="skill-tag">Bootstrap</span>
                            <span class="skill-tag">JavaScript</span>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </div>

    <!-- Contact -->
    <section class="section">
        <div class="container">
            <div class="section-title">Contact</div>
            <div class="contact-grid">
                <div class="contact-item">
                    <h4>Email</h4>
                    <p>joy981017@gmail.com</p>
                </div>
                <div class="contact-item">
                    <h4>GitHub</h4>
                    <p>github.com/joyuno</p>
                </div>
                <div class="contact-item">
                    <h4>Location</h4>
                    <p>Seoul, Korea</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <p>&copy; 2025 Yunho Jang. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
"""

# Save HTML
output_html = BASE_PATH / "portfolio_full.html"
with open(output_html, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"HTML generated: {output_html}")

# Generate PDF
from weasyprint import HTML, CSS

output_pdf = BASE_PATH / "Yunho_Jang_Portfolio.pdf"
HTML(string=html_content, base_url=str(BASE_PATH)).write_pdf(output_pdf)
print(f"PDF generated: {output_pdf}")
