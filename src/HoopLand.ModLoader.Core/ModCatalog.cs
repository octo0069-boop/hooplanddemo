using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text.Json;
using HoopLand.ModLoader;

namespace HoopLand.ModLoader.Core;

public sealed class ModCatalog
{
    private static readonly JsonSerializerOptions JsonOptions = new()
    {
        PropertyNameCaseInsensitive = true
    };

    public IReadOnlyList<ModDescriptor> Discover(string modsDirectory)
    {
        if (!Directory.Exists(modsDirectory))
            return Array.Empty<ModDescriptor>();

        var found = new List<ModDescriptor>();
        foreach (var directory in Directory.GetDirectories(modsDirectory))
        {
            var manifestPath = Path.Combine(directory, "mod.json");
            if (!File.Exists(manifestPath))
                continue;

            try
            {
                var json = File.ReadAllText(manifestPath);
                var descriptor = JsonSerializer.Deserialize<ModDescriptor>(json, JsonOptions);
                if (descriptor != null && !string.IsNullOrWhiteSpace(descriptor.Id))
                    found.Add(descriptor);
            }
            catch (JsonException)
            {
                // Invalid manifests are skipped; callers can add diagnostics around discovery.
            }
        }

        return found.OrderBy(x => x.Id, StringComparer.OrdinalIgnoreCase).ToArray();
    }
}
