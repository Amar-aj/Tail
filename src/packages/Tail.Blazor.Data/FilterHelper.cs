using System.Linq.Expressions;
using Tail.Blazor.Data.Models;

namespace Tail.Blazor.Data;

/// <summary>
/// Helper class for applying filter conditions to data.
/// </summary>
public static class FilterHelper
{
    /// <summary>
    /// Applies filter conditions to a collection of items.
    /// </summary>
    public static IEnumerable<T> ApplyFilters<T>(this IEnumerable<T> items, List<FilterCondition> conditions)
    {
        if (conditions == null || !conditions.Any() || items == null)
            return items;

        var filtered = items.AsEnumerable();
        var firstCondition = true;

        foreach (var condition in conditions.Where(c => !string.IsNullOrEmpty(c.Column)))
        {
            var property = typeof(T).GetProperty(condition.Column);
            if (property == null) continue;

            var conditionExpression = BuildConditionExpression<T>(condition, property);
            if (conditionExpression == null) continue;

            if (firstCondition)
            {
                filtered = filtered.Where(conditionExpression.Compile());
                firstCondition = false;
            }
            else
            {
                if (condition.Logic == FilterLogic.And)
                {
                    filtered = filtered.Where(conditionExpression.Compile());
                }
                else // Or
                {
                    var original = filtered.ToList();
                    var additional = items.Where(conditionExpression.Compile());
                    filtered = original.Union(additional);
                }
            }
        }

        return filtered;
    }

    private static Expression<Func<T, bool>>? BuildConditionExpression<T>(FilterCondition condition, System.Reflection.PropertyInfo property)
    {
        var parameter = Expression.Parameter(typeof(T), "x");
        var propertyAccess = Expression.Property(parameter, property);
        var constant = Expression.Constant(condition.Value);

        Expression? comparison = null;

        switch (condition.Operator)
        {
            case FilterOperator.Equals:
                comparison = Expression.Equal(propertyAccess, constant);
                break;
            case FilterOperator.NotEquals:
                comparison = Expression.NotEqual(propertyAccess, constant);
                break;
            case FilterOperator.Contains:
                if (property.PropertyType == typeof(string) && condition.Value is string strValue)
                {
                    var containsMethod = typeof(string).GetMethod("Contains", new[] { typeof(string) });
                    if (containsMethod != null)
                    {
                        var containsConstant = Expression.Constant(strValue, typeof(string));
                        comparison = Expression.Call(propertyAccess, containsMethod, containsConstant);
                    }
                }
                break;
            case FilterOperator.NotContains:
                if (property.PropertyType == typeof(string) && condition.Value is string notContainsValue)
                {
                    var containsMethod = typeof(string).GetMethod("Contains", new[] { typeof(string) });
                    if (containsMethod != null)
                    {
                        var containsConstant = Expression.Constant(notContainsValue, typeof(string));
                        var containsCall = Expression.Call(propertyAccess, containsMethod, containsConstant);
                        comparison = Expression.Not(containsCall);
                    }
                }
                break;
            case FilterOperator.StartsWith:
                if (property.PropertyType == typeof(string) && condition.Value is string startsValue)
                {
                    var startsWithMethod = typeof(string).GetMethod("StartsWith", new[] { typeof(string) });
                    if (startsWithMethod != null)
                    {
                        var startsConstant = Expression.Constant(startsValue, typeof(string));
                        comparison = Expression.Call(propertyAccess, startsWithMethod, startsConstant);
                    }
                }
                break;
            case FilterOperator.EndsWith:
                if (property.PropertyType == typeof(string) && condition.Value is string endsValue)
                {
                    var endsWithMethod = typeof(string).GetMethod("EndsWith", new[] { typeof(string) });
                    if (endsWithMethod != null)
                    {
                        var endsConstant = Expression.Constant(endsValue, typeof(string));
                        comparison = Expression.Call(propertyAccess, endsWithMethod, endsConstant);
                    }
                }
                break;
            case FilterOperator.GreaterThan:
                comparison = Expression.GreaterThan(propertyAccess, constant);
                break;
            case FilterOperator.GreaterThanOrEqual:
                comparison = Expression.GreaterThanOrEqual(propertyAccess, constant);
                break;
            case FilterOperator.LessThan:
                comparison = Expression.LessThan(propertyAccess, constant);
                break;
            case FilterOperator.LessThanOrEqual:
                comparison = Expression.LessThanOrEqual(propertyAccess, constant);
                break;
            case FilterOperator.IsEmpty:
                if (property.PropertyType == typeof(string))
                {
                    comparison = Expression.Equal(propertyAccess, Expression.Constant(string.Empty));
                }
                break;
            case FilterOperator.IsNotEmpty:
                if (property.PropertyType == typeof(string))
                {
                    comparison = Expression.NotEqual(propertyAccess, Expression.Constant(string.Empty));
                }
                break;
        }

        if (comparison == null) return null;

        return Expression.Lambda<Func<T, bool>>(comparison, parameter);
    }
}

