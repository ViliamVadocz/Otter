use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

/// example function
#[pyfunction]
fn add_1(x: i64) -> i64 {
    x + 1
}

/// exported module
#[pymodule]
fn rust_utils(py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(simulate_jump, m)?)?;

    Ok(())
}
