def summarize_by_category(expenses):
    summary = {}

    for expense in expenses:
        if expense.category in summary:
            summary[expense.category] += expense.amount
        else:
            summary[expense.category] = expense.amount

    return summary
