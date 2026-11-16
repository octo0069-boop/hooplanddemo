using System;
using System.Collections.Generic;

namespace HoopLand.ModLoader;

public interface IHoopLandMod
{
    string Id { get; }
    string Version { get; }
    void Load(IModContext context);
    void Unload();
}

public interface IModContext
{
    IModLogger Logger { get; }
    IContentRegistry Content { get; }
    IAssetRegistry Assets { get; }
}

public interface IModLogger
{
    void Info(string message);
    void Warn(string message);
    void Error(string message, Exception? exception = null);
}

public interface IContentRegistry
{
    void Register(string contentKind, string contentId, object definition);
}

public interface IAssetRegistry
{
    void Override(string logicalAssetId, string relativeFilePath);
}

public interface IRuntimeBackend
{
    string Name { get; }
    bool IsAvailable { get; }
    void Initialize();
    void Shutdown();
    void RegisterContent(string contentKind, string contentId, object definition);
    void OverrideAsset(string logicalAssetId, string relativeFilePath);
}

public sealed class ModDescriptor
{
    public string Id { get; set; } = "";
    public string Version { get; set; } = "1.0.0";
    public string DisplayName { get; set; } = "";
    public string EntryAssembly { get; set; } = "";
    public List<string> Dependencies { get; set; } = new();
}
