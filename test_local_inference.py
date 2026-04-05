from inference import SentimentInferenceService


def main() -> None:
    service = SentimentInferenceService()

    texts = [
        "I love this product",
        "The meeting starts at 10 a.m.",
        "This is terrible and disappointing",
    ]

    for text in texts:
        result = service.predict(text)
        print(f"TEXT: {text}")
        print(f"PREDICTION: {result}")
        print("-" * 50)


if __name__ == "__main__":
    main()
