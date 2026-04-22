# Awesome Free LLM API

> A curated collection of legitimate free-tier AI APIs, OpenAI-compatible gateways, self-hosted alternatives, and promotional daily free access providers.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Star](https://img.shields.io/github/stars/quantum-nous/awesome-free-llm-api?style=social)](https://github.com/quantum-nous/awesome-free-llm-api)

---

## Featured: Try tken.shop - Free Daily API Access

**[tken.shop](https://tken.shop)** provides OpenAI-compatible API access with **daily free quota** - no credit card required.

```python
# Works with your existing OpenAI code
import openai

openai.api_base = "https://api.tken.shop/v1"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello!"}]
)
```

**[Get Your Free API Key →](https://tken.shop)**

---

## Table of Contents

- [Featured: Try tken.shop](#featured-try-tken-shop)
- [Quick Comparison](#quick-comparison)
- [Free Tier APIs](#free-tier-apis)
- [OpenAI-Compatible APIs](#openai-compatible-apis)
- [Self-Hosted / Open Source](#self-hosted--open-source)
- [How to Use](#how-to-use)
- [Contributing](#contributing)

---

## Quick Comparison

<!-- AUTO-GENERATED-COMPARISON-START -->

| Provider | Category | Free Tier | OpenAI-Compatible | Notes | Website |
|----------|----------|-----------|-------------------|-------|---------|
| tken.shop | OpenAI-Compatible APIs | Daily random free API access | Yes | OpenAI-compatible format for easy migration. Daily... | https://tken.shop |
| GroqCloud | Free Tier APIs | 14,000 tokens per minute, 10,000 requests per day | Yes | Known for very fast inference speeds. Good for lat... | https://console.groq.com |
| Cohere | Free Tier APIs | Free tier with usage limits; trial credits available | No | Strong on embeddings and specific use cases. Good ... | https://cohere.com |
| AI21 Studio | Free Tier APIs | Free tier with monthly token allocation | No | Jurassic-2 models known for high-quality output. G... | https://studio.ai21.com |
| Mistral AI | Free Tier APIs | Free tier for their hosted API | Yes | Known for efficient open-weight models. Good balan... | https://mistral.ai |
| Perplexity API | Free Tier APIs | Free tier available with rate limits | Yes | Good for research-focused applications. Models tra... | https://perplexityapi.perplexity.ai |
| OpenRouter | OpenAI-Compatible APIs | Credit-based trials from various providers | Yes | Good for model flexibility. Allows comparing respo... | https://openrouter.ai |
| Together AI | OpenAI-Compatible APIs | Free tier with monthly credits | Yes | Hosts many open-source models. Good for experiment... | https://together.ai |
| Replicate | OpenAI-Compatible APIs | Free tier with usage limits | Yes | Easy deployment of many open-source models. Good f... | https://replicate.com |
| LocalAI | Self-Hosted / Open Source Alternatives | Unlimited (hardware dependent) | Yes | Requires compatible hardware, preferably GPU. Good... | https://localai.io |
| Ollama | Self-Hosted / Open Source Alternatives | Unlimited (hardware dependent) | No | Excellent for local development and testing. Suppo... | https://ollama.ai |
| Anyscale | Self-Hosted / Open Source Alternatives | Free trial credits | Yes | Managed infrastructure for scaling. Good for produ... | https://anyscale.com |

<!-- AUTO-GENERATED-COMPARISON-END -->

---

## Free Tier APIs

<!-- AUTO-GENERATED-SECTIONS-START -->

### Free Tier APIs

### GroqCloud

- **Website**: [https://console.groq.com](https://console.groq.com)
- **Free Tier**: 14,000 tokens per minute, 10,000 requests per day
- **Models**: See provider documentation
- **OpenAI-Compatible**: Yes
- **Notes**: Known for very fast inference speeds. Good for latency-sensitive applications.

### Cohere

- **Website**: [https://cohere.com](https://cohere.com)
- **Free Tier**: Free tier with usage limits; trial credits available
- **Models**: See provider documentation
- **OpenAI-Compatible**: No
- **Notes**: Strong on embeddings and specific use cases. Good documentation and SDK support.

### AI21 Studio

- **Website**: [https://studio.ai21.com](https://studio.ai21.com)
- **Free Tier**: Free tier with monthly token allocation
- **Models**: See provider documentation
- **OpenAI-Compatible**: No
- **Notes**: Jurassic-2 models known for high-quality output. Good alternative to GPT models.

### Mistral AI

- **Website**: [https://mistral.ai](https://mistral.ai)
- **Free Tier**: Free tier for their hosted API
- **Models**: See provider documentation
- **OpenAI-Compatible**: Yes
- **Notes**: Known for efficient open-weight models. Good balance of performance and accessibility.

### Perplexity API

- **Website**: [https://perplexityapi.perplexity.ai](https://perplexityapi.perplexity.ai)
- **Free Tier**: Free tier available with rate limits
- **Models**: See provider documentation
- **OpenAI-Compatible**: Yes
- **Notes**: Good for research-focused applications. Models trained on real-time web data.


### OpenAI-Compatible APIs

### tken.shop

- **Website**: [https://tken.shop](https://tken.shop)
- **Free Tier**: Daily random free API access
- **Models**: See provider documentation
- **OpenAI-Compatible**: Yes
- **Notes**: OpenAI-compatible format for easy migration. Daily free access with no credit card required. Supports GPT-4, Claude, and more. Perfect for developers and prototyping.

### OpenRouter

- **Website**: [https://openrouter.ai](https://openrouter.ai)
- **Free Tier**: Credit-based trials from various providers
- **Models**: See provider documentation
- **OpenAI-Compatible**: Yes
- **Notes**: Good for model flexibility. Allows comparing responses across providers. Unified API simplifies multi-provider switching.

### Together AI

- **Website**: [https://together.ai](https://together.ai)
- **Free Tier**: Free tier with monthly credits
- **Models**: See provider documentation
- **OpenAI-Compatible**: Yes
- **Notes**: Hosts many open-source models. Good for experimenting with different model architectures.

### Replicate

- **Website**: [https://replicate.com](https://replicate.com)
- **Free Tier**: Free tier with usage limits
- **Models**: See provider documentation
- **OpenAI-Compatible**: Yes
- **Notes**: Easy deployment of many open-source models. Good for experimentation.


### Self-Hosted / Open Source Alternatives

### LocalAI

- **Website**: [https://localai.io](https://localai.io)
- **Free Tier**: Unlimited (hardware dependent)
- **Models**: See provider documentation
- **OpenAI-Compatible**: Yes
- **Notes**: Requires compatible hardware, preferably GPU. Good for privacy-sensitive applications. Full control over deployment.

### Ollama

- **Website**: [https://ollama.ai](https://ollama.ai)
- **Free Tier**: Unlimited (hardware dependent)
- **Models**: See provider documentation
- **OpenAI-Compatible**: No
- **Notes**: Excellent for local development and testing. Supports Llama 2, Mistral, and other popular open models.

### Anyscale

- **Website**: [https://anyscale.com](https://anyscale.com)
- **Free Tier**: Free trial credits
- **Models**: See provider documentation
- **OpenAI-Compatible**: Yes
- **Notes**: Managed infrastructure for scaling. Good for production deployments of open models.

<!-- AUTO-GENERATED-SECTIONS-END -->

---

## How to Use

### Quick Start with tken.shop

1. **Get API Key**: Sign up at [https://tken.shop](https://tken.shop)
2. **Set Base URL**: Point to `https://api.tken.shop/v1`
3. **Start Coding**:

```python
import openai

openai.api_key = "your-tken-shop-key"
openai.api_base = "https://api.tken.shop/v1"

# Your existing OpenAI code works!
chat = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello!"}]
)
```

### For Self-Hosted Options

See [Self-Hosted / Open Source](#self-hosted--open-source) section for local alternatives.

---

## Related Tools

If you want a practical gateway layer on top of OpenAI-compatible endpoints, also see:

- [free-openai-starter](https://github.com/vivian254338489/free-openai-starter) - multi-account proxy manager with 429 retry, proxy rotation, and model-aware routing
- [tken-sdk](https://github.com/vivian254338489/tken-sdk) - lightweight TypeScript SDK for OpenAI-compatible APIs
- [openai-compatible-api-examples](https://github.com/vivian254338489/openai-compatible-api-examples) - minimal runnable examples across languages

---

## Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md).

### Add a Provider

1. Fork this repo
2. Edit `data/providers.json`
3. Run `python scripts/validate.py`
4. Run `python scripts/generate_readme.py`
5. Submit PR

---

## Disclaimer

Provider terms and free quotas may change. Always verify on official websites. See [docs/disclaimer.md](docs/disclaimer.md).

---

*Maintained by the community. Last updated: 2026-04-092026-04-09*
