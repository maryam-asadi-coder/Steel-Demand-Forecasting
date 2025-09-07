import streamlit as st
import pandas as pd
import numpy as np
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import plotly.graph_objects as go

# =============================
# تنظیمات صفحه
# =============================
st.set_page_config(page_title="Steel Demand Forecast & Inventory Dashboard", layout="wide")
st.title("Steel Demand Forecast & Inventory Dashboard")

# =============================
# داده نمونه شبیه‌سازی‌شده
# =============================
np.random.seed(42)
# فرکانس مشخص شده: هفته‌ای از دوشنبه
dates = pd.date_range(start="2025-01-01", periods=52, freq="W-MON")
demand = np.random.randint(80, 120, size=len(dates))
inventory = np.random.randint(50, 100, size=len(dates))
data = pd.DataFrame({"Date": dates, "Demand": demand, "Inventory": inventory})
data.set_index("Date", inplace=True)

st.subheader("Raw Data")
st.dataframe(data)

# =============================
# پیش‌بینی تقاضا 12 هفته آینده
# =============================
model = ExponentialSmoothing(data["Demand"], trend="add", seasonal="add", seasonal_periods=12)
fit = model.fit()
forecast = fit.forecast(12)
forecast_index = pd.date_range(start=data.index[-1] + pd.Timedelta(weeks=1), periods=12, freq="W-MON")
forecast_series = pd.Series(forecast, index=forecast_index)

st.subheader("12-Week Demand Forecast")
fig_forecast = go.Figure()
fig_forecast.add_trace(go.Scatter(x=data.index, y=data["Demand"], mode="lines+markers", name="Actual Demand"))
fig_forecast.add_trace(go.Scatter(x=forecast_series.index, y=forecast_series, mode="lines+markers", name="Forecast Demand"))
st.plotly_chart(fig_forecast, use_container_width=True)

# =============================
# محاسبه Safety Stock و Reorder Point
# =============================
lead_time_weeks = 4
std_dev = data["Demand"].std()
avg_demand = data["Demand"].mean()

Z = 1.65  # سطح اطمینان 95٪
safety_stock = Z * std_dev * np.sqrt(lead_time_weeks)
reorder_point = avg_demand * lead_time_weeks + safety_stock

st.subheader("Inventory Recommendations")
st.metric("Safety Stock", f"{int(safety_stock)} units")
st.metric("Reorder Point", f"{int(reorder_point)} units")

# =============================
# KPIها
# =============================
avg_otif = np.random.uniform(88, 97)
waste_reduction = np.random.uniform(10, 15)
st.subheader("Key Performance Indicators (KPIs)")
st.metric("OTIF", f"{avg_otif:.1f}%")
st.metric("Estimated Waste Reduction", f"{waste_reduction:.1f}%")

# =============================
# نمودار نهایی: Demand vs Inventory vs Forecast vs Safety/Reorder
# =============================
fig_inventory = go.Figure()
fig_inventory.add_trace(go.Scatter(x=data.index, y=data["Demand"], mode="lines+markers", name="Actual Demand"))
fig_inventory.add_trace(go.Scatter(x=forecast_series.index, y=forecast_series, mode="lines+markers", name="Forecast Demand"))
fig_inventory.add_trace(go.Scatter(x=data.index, y=data["Inventory"], mode="lines+markers", name="Inventory"))
fig_inventory.add_trace(go.Scatter(x=forecast_series.index, y=[reorder_point]*len(forecast_series), mode="lines", name="Reorder Point", line=dict(dash="dash", color="red")))
fig_inventory.add_trace(go.Scatter(x=forecast_series.index, y=[safety_stock]*len(forecast_series), mode="lines", name="Safety Stock", line=dict(dash="dot", color="green")))

fig_inventory.update_layout(
    title="Steel Demand, Inventory & Safety/Reorder Levels",
    xaxis_title="Date",
    yaxis_title="Units",
    template="plotly_white"
)
st.plotly_chart(fig_inventory, use_container_width=True)
