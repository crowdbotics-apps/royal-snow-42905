import { createSlice, createAsyncThunk } from "@reduxjs/toolkit"
import { apiService } from "./api"
export const api_v1_businessrule_list = createAsyncThunk(
  "businessRules/api_v1_businessrule_list",
  async payload => {
    const response = await apiService.api_v1_businessrule_list(payload)
    return response.data
  }
)
export const api_v1_businessrule_create = createAsyncThunk(
  "businessRules/api_v1_businessrule_create",
  async payload => {
    const response = await apiService.api_v1_businessrule_create(payload)
    return response.data
  }
)
export const api_v1_businessrule_retrieve = createAsyncThunk(
  "businessRules/api_v1_businessrule_retrieve",
  async payload => {
    const response = await apiService.api_v1_businessrule_retrieve(payload)
    return response.data
  }
)
export const api_v1_businessrule_update = createAsyncThunk(
  "businessRules/api_v1_businessrule_update",
  async payload => {
    const response = await apiService.api_v1_businessrule_update(payload)
    return response.data
  }
)
export const api_v1_businessrule_partial_update = createAsyncThunk(
  "businessRules/api_v1_businessrule_partial_update",
  async payload => {
    const response = await apiService.api_v1_businessrule_partial_update(
      payload
    )
    return response.data
  }
)
export const api_v1_businessrule_destroy = createAsyncThunk(
  "businessRules/api_v1_businessrule_destroy",
  async payload => {
    const response = await apiService.api_v1_businessrule_destroy(payload)
    return response.data
  }
)
const initialState = { entities: [], api: { loading: "idle", error: null } }
const businessRulesSlice = createSlice({
  name: "businessRules",
  initialState,
  reducers: {},
  extraReducers: {
    [api_v1_businessrule_list.pending]: (state, action) => {
      if (state.api.loading === "idle") {
        state.api.loading = "pending"
      }
    },
    [api_v1_businessrule_list.fulfilled]: (state, action) => {
      if (state.api.loading === "pending") {
        state.entities = action.payload
        state.api.loading = "idle"
      }
    },
    [api_v1_businessrule_list.rejected]: (state, action) => {
      if (state.api.loading === "pending") {
        state.api.error = action.error
        state.api.loading = "idle"
      }
    },
    [api_v1_businessrule_create.pending]: (state, action) => {
      if (state.api.loading === "idle") {
        state.api.loading = "pending"
      }
    },
    [api_v1_businessrule_create.fulfilled]: (state, action) => {
      if (state.api.loading === "pending") {
        state.entities.push(action.payload)
        state.api.loading = "idle"
      }
    },
    [api_v1_businessrule_create.rejected]: (state, action) => {
      if (state.api.loading === "pending") {
        state.api.error = action.error
        state.api.loading = "idle"
      }
    },
    [api_v1_businessrule_retrieve.pending]: (state, action) => {
      if (state.api.loading === "idle") {
        state.api.loading = "pending"
      }
    },
    [api_v1_businessrule_retrieve.fulfilled]: (state, action) => {
      if (state.api.loading === "pending") {
        state.entities = [
          ...state.entities.filter(record => record.id !== action.payload.id),
          action.payload
        ]
        state.api.loading = "idle"
      }
    },
    [api_v1_businessrule_retrieve.rejected]: (state, action) => {
      if (state.api.loading === "pending") {
        state.api.error = action.error
        state.api.loading = "idle"
      }
    },
    [api_v1_businessrule_update.pending]: (state, action) => {
      if (state.api.loading === "idle") {
        state.api.loading = "pending"
      }
    },
    [api_v1_businessrule_update.fulfilled]: (state, action) => {
      if (state.api.loading === "pending") {
        state.entities = state.entities.map(record =>
          record.id === action.payload.id ? action.payload : record
        )
        state.api.loading = "idle"
      }
    },
    [api_v1_businessrule_update.rejected]: (state, action) => {
      if (state.api.loading === "pending") {
        state.api.error = action.error
        state.api.loading = "idle"
      }
    },
    [api_v1_businessrule_partial_update.pending]: (state, action) => {
      if (state.api.loading === "idle") {
        state.api.loading = "pending"
      }
    },
    [api_v1_businessrule_partial_update.fulfilled]: (state, action) => {
      if (state.api.loading === "pending") {
        state.entities = state.entities.map(record =>
          record.id === action.payload.id ? action.payload : record
        )
        state.api.loading = "idle"
      }
    },
    [api_v1_businessrule_partial_update.rejected]: (state, action) => {
      if (state.api.loading === "pending") {
        state.api.error = action.error
        state.api.loading = "idle"
      }
    },
    [api_v1_businessrule_destroy.pending]: (state, action) => {
      if (state.api.loading === "idle") {
        state.api.loading = "pending"
      }
    },
    [api_v1_businessrule_destroy.fulfilled]: (state, action) => {
      if (state.api.loading === "pending") {
        state.entities = state.entities.filter(
          record => record.id !== action.meta.arg?.id
        )
        state.api.loading = "idle"
      }
    },
    [api_v1_businessrule_destroy.rejected]: (state, action) => {
      if (state.api.loading === "pending") {
        state.api.error = action.error
        state.api.loading = "idle"
      }
    }
  }
})
export default {
  api_v1_businessrule_list,
  api_v1_businessrule_create,
  api_v1_businessrule_retrieve,
  api_v1_businessrule_update,
  api_v1_businessrule_partial_update,
  api_v1_businessrule_destroy,
  slice: businessRulesSlice
}
