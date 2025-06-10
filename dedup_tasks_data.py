import pandas as pd


def load_tasks(filepath: str) -> pd.DataFrame:
    """Load task data from an Excel file."""
    return pd.read_excel(filepath)

def normalize_and_deduplicate(df: pd.DataFrame) -> pd.DataFrame:
    """Normalize task titles and remove duplicates."""
    df["normalized_title"] = df["Title"].str.strip().str.lower()
    deduped = df.drop_duplicates(subset=["normalized_title"]).copy()
    deduped.drop(columns=["normalized_title"], inplace=True)
    return deduped

def summarize_tasks(original_df: pd.DataFrame, deduped_df: pd.DataFrame) -> tuple[int, int]:
    """Return total and unique task counts."""
    return original_df.shape[0], deduped_df.shape[0]

def save_tasks(df: pd.DataFrame, output_path: str) -> None:
    """Export the cleaned task list to an Excel file."""
    df.to_excel(output_path, index=False)

def main():
    input_path = "tasks_report_2025-05-20-14-11-41.xlsx"
    output_path = "deduplicated_tasks.xlsx"

    df = load_tasks(input_path)
    deduped_df = normalize_and_deduplicate(df)
    total, unique = summarize_tasks(df, deduped_df)

    print(f"Total tasks: {total}")
    print(f"Unique tasks: {unique}")

    save_tasks(deduped_df, output_path)
    print(f"Deduplicated tasks saved to: {output_path}")

if __name__ == "__main__":
    main()
